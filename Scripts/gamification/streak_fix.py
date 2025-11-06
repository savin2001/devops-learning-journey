#!/usr/bin/env python3
"""
Streak Fix for DevOps XP Tracker
This module provides streak tracking that accounts for scheduled study days only.
"""

from datetime import datetime, timedelta
import json
import os

class ScheduledStreakTracker:
    """
    Tracks streaks based on scheduled study days only.
    Study days: Tuesday (1), Thursday (3), Saturday (5), Sunday (6)
    """

    # Your scheduled study days (0=Monday, 1=Tuesday, ..., 6=Sunday)
    STUDY_DAYS = [1, 3, 5, 6]  # Tuesday, Thursday, Saturday, Sunday

    def __init__(self, data_file="xp_data.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """Load progress data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("⚠️  Warning: Could not read data file.")
        return None

    def save_data(self):
        """Save progress data to JSON file"""
        if self.data:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
            print("💾 Streak data updated!")

    def get_previous_study_day(self, from_date):
        """Get the previous scheduled study day before from_date"""
        current = from_date - timedelta(days=1)
        while current.weekday() not in self.STUDY_DAYS:
            current -= timedelta(days=1)
        return current

    def get_next_study_day(self, from_date):
        """Get the next scheduled study day after from_date"""
        current = from_date + timedelta(days=1)
        while current.weekday() not in self.STUDY_DAYS:
            current += timedelta(days=1)
        return current

    def is_study_day(self, date):
        """Check if the given date is a scheduled study day"""
        return date.weekday() in self.STUDY_DAYS

    def missed_any_study_days(self, last_date, current_date):
        """
        Check if any scheduled study days were missed between last_date and current_date.
        Returns (missed: bool, expected_day: date)
        """
        if last_date >= current_date:
            return False, None

        # Get the expected next study day after last_date
        expected_next = self.get_next_study_day(last_date)

        # If current_date is before or on expected_next, no days were missed
        if current_date <= expected_next:
            return False, None

        # If current_date is after expected_next, we missed at least one study day
        return True, expected_next

    def update_streak(self, study_date=None):
        """
        Update study streak based on scheduled study days.
        Only counts missed SCHEDULED study days as streak breaks.
        """
        if not self.data:
            print("❌ No data file found. Please run the XP tracker first.")
            return

        if study_date is None:
            study_date = datetime.now().date()
        else:
            study_date = datetime.fromisoformat(study_date).date() if isinstance(study_date, str) else study_date

        # Check if today is a study day
        if not self.is_study_day(study_date):
            print(f"📅 {study_date.strftime('%A')} is not a scheduled study day.")
            print(f"📚 Your study days are: Tuesday, Thursday, Saturday, Sunday")
            print(f"⏭️  Next study day: {self.get_next_study_day(study_date).strftime('%A, %B %d')}")
            return

        last_date = None
        if self.data['last_study_date']:
            last_date = datetime.fromisoformat(self.data['last_study_date']).date()

        if last_date is None:
            # First study day
            self.data['current_streak'] = 1
            self.data['last_study_date'] = study_date.isoformat()
            self.save_data()
            print("🔥 Streak started: 1 study session!")
            print(f"⏭️  Next study session: {self.get_next_study_day(study_date).strftime('%A, %B %d')}")

        elif study_date == last_date:
            # Same day - already logged
            print(f"✅ Already logged today! Current streak: {self.data['current_streak']} sessions")

        else:
            # Check if any scheduled study days were missed
            missed, expected_day = self.missed_any_study_days(last_date, study_date)

            if missed:
                # Streak broken - missed a scheduled study day
                old_streak = self.data['current_streak']
                print(f"❌ Streak broken! You missed {expected_day.strftime('%A, %B %d')}")
                print(f"   Previous streak: {old_streak} sessions")
                print(f"💡 Starting fresh. You can do it!")
                self.data['current_streak'] = 1
            else:
                # Continuing streak - no scheduled days were missed
                self.data['current_streak'] += 1
                streak = self.data['current_streak']
                print(f"🔥 Streak continues: {streak} sessions!")

                # Update longest streak
                if streak > self.data.get('longest_streak', 0):
                    self.data['longest_streak'] = streak
                    print(f"🏆 New personal best!")

            self.data['last_study_date'] = study_date.isoformat()
            self.save_data()
            print(f"⏭️  Next study session: {self.get_next_study_day(study_date).strftime('%A, %B %d')}")

    def view_schedule(self):
        """Display your study schedule for the current week"""
        today = datetime.now().date()

        # Find Monday of this week
        monday = today - timedelta(days=today.weekday())

        print("\n📅 YOUR WEEKLY STUDY SCHEDULE")
        print("="*50)

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        for i, day_name in enumerate(days):
            day_date = monday + timedelta(days=i)
            is_today = (day_date == today)
            is_study = i in self.STUDY_DAYS

            marker = "📚" if is_study else "  "
            today_marker = " ← TODAY" if is_today else ""

            print(f"{marker} {day_name:12} - {day_date.strftime('%b %d')}{today_marker}")

        print("="*50)
        print("📚 = Study Day | 4 sessions per week\n")

def main():
    """Interactive streak fix tool"""
    tracker = ScheduledStreakTracker()

    while True:
        print("\n" + "="*50)
        print("🔥 SCHEDULED STREAK TRACKER 🔥".center(50))
        print("="*50)
        print("\n1. 📅 View Study Schedule")
        print("2. 🔥 Update Streak (Today)")
        print("3. 🔄 Fix Streak (Custom Date)")
        print("4. 📊 View Current Streak")
        print("0. ❌ Exit")
        print("="*50)

        choice = input("\nChoice (0-4): ").strip()

        if choice == '1':
            tracker.view_schedule()

        elif choice == '2':
            tracker.update_streak()

        elif choice == '3':
            date_str = input("Enter date (YYYY-MM-DD): ").strip()
            try:
                tracker.update_streak(date_str)
            except ValueError:
                print("❌ Invalid date format. Use YYYY-MM-DD")

        elif choice == '4':
            if tracker.data:
                streak = tracker.data.get('current_streak', 0)
                longest = tracker.data.get('longest_streak', 0)
                last_date = tracker.data.get('last_study_date', 'Never')

                if last_date != 'Never':
                    last_date = datetime.fromisoformat(last_date).strftime('%A, %B %d, %Y')

                print(f"\n🔥 Current Streak: {streak} sessions")
                print(f"🏆 Longest Streak: {longest} sessions")
                print(f"📅 Last Study: {last_date}")
            else:
                print("❌ No data found")

        elif choice == '0':
            print("\n👋 Keep the streak alive!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
