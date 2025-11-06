# 🔥 Streak Tracking Fix - Scheduled Study Days

## The Problem

The original XP tracker counts **consecutive calendar days** for streaks. This causes issues when you have a scheduled study routine:

### Your Study Schedule:
- **Tuesday** - Evening session (1.5 hrs)
- **Thursday** - Evening session (1.5 hrs)
- **Saturday** - Morning session (3 hrs)
- **Sunday** - Afternoon session (3 hrs)

### What Happens:
1. ✅ Study on Tuesday (Nov 4) → Streak = 1 day
2. ⏸️ Wednesday is not a study day (skip)
3. ✅ Study on Thursday (Nov 6) → **Streak broken!** ❌

The system thinks you "missed" Wednesday, but Wednesday was never a study day!

## The Solution

The `streak_fix.py` script tracks streaks based on **scheduled study days only**. It knows your study days are Tuesday, Thursday, Saturday, and Sunday, so it only counts those.

### How It Works:
1. ✅ Study on Tuesday → Streak = 1 session
2. ⏸️ Wednesday (not a study day, doesn't count)
3. ✅ Study on Thursday → Streak = 2 sessions ✅
4. ⏸️ Friday (not a study day, doesn't count)
5. ✅ Study on Saturday → Streak = 3 sessions ✅
6. ✅ Study on Sunday → Streak = 4 sessions ✅

Only if you **miss a scheduled study day** will your streak break.

## Installation & Usage

### Quick Start (Windows):

```bash
# Navigate to the gamification folder
cd Scripts/gamification

# Run the streak fix tool
python streak_fix.py

# Or use the batch file
streak.bat
```

### Menu Options:

```
🔥 SCHEDULED STREAK TRACKER 🔥

1. 📅 View Study Schedule    - See your weekly study days
2. 🔥 Update Streak (Today)  - Log today's study session
3. 🔄 Fix Streak (Custom)    - Update streak for a past date
4. 📊 View Current Streak    - Check your current stats
0. ❌ Exit
```

## Examples

### Example 1: Normal Week (No Missed Days)

```
Tuesday (Nov 4):    Study ✅ → Streak: 1
Wednesday:          Not a study day (skip)
Thursday (Nov 7):   Study ✅ → Streak: 2
Friday:             Not a study day (skip)
Saturday (Nov 9):   Study ✅ → Streak: 3
Sunday (Nov 10):    Study ✅ → Streak: 4

Result: Perfect week! 🔥🔥🔥🔥
```

### Example 2: Missed Thursday

```
Tuesday (Nov 4):    Study ✅ → Streak: 1
Wednesday:          Not a study day (skip)
Thursday (Nov 7):   Missed ❌
Friday:             Not a study day (skip)
Saturday (Nov 9):   Study ❌ → STREAK BROKEN (missed Thursday)
                    New streak starts: 1

Result: Streak broken because you missed a SCHEDULED day
```

## Updating Your Schedule

If your study schedule changes, edit the `STUDY_DAYS` list in `streak_fix.py`:

```python
# Your scheduled study days (0=Monday, 1=Tuesday, ..., 6=Sunday)
STUDY_DAYS = [1, 3, 5, 6]  # Tuesday, Thursday, Saturday, Sunday
```

### Day Numbers:
- 0 = Monday
- 1 = Tuesday
- 2 = Wednesday
- 3 = Thursday
- 4 = Friday
- 5 = Saturday
- 6 = Sunday

### Example Schedules:

**Every weekday:**
```python
STUDY_DAYS = [0, 1, 2, 3, 4]  # Mon-Fri
```

**Weekends only:**
```python
STUDY_DAYS = [5, 6]  # Sat-Sun
```

**Custom schedule:**
```python
STUDY_DAYS = [1, 3, 5]  # Tue, Thu, Sat
```

## Integration with XP Tracker

The streak fix tool reads and updates the same `xp_data.json` file used by your XP tracker. You can use both tools together:

1. **For logging XP and activities** → Use `xp_tracker_v2.py` or `xp.bat`
2. **For accurate streak tracking** → Use `streak_fix.py` or `streak.bat`

## Recommended Workflow

### Option 1: Use Streak Fix Only
Use the streak fix tool whenever you complete a study session. It only updates streaks, not XP.

### Option 2: Fix After XP Logging
1. Log your session with the regular XP tracker: `./xp q`
2. If it says "Streak broken" incorrectly, run: `python streak_fix.py`
3. Choose option 2 to update today's streak properly

### Option 3: Backfill Streaks
If you've already logged several sessions with broken streaks:
1. Run `python streak_fix.py`
2. Choose option 3 (Fix Streak - Custom Date)
3. Enter each study date to rebuild your streak accurately

## Current Status

Based on your schedule (Tuesday, Thursday, Saturday, Sunday):

```
Week 1 Progress:
✅ Nov 4 (Tuesday)    - Session 1 complete
✅ Nov 7 (Thursday)   - Session 2 complete
⏳ Nov 9 (Saturday)   - Session 3 upcoming
⏳ Nov 10 (Sunday)    - Session 4 upcoming

Current: 2/4 sessions this week
Actual Streak: 2 sessions (not broken!)
```

## Benefits of This Approach

1. ✅ **More Accurate** - Reflects your actual study routine
2. ✅ **More Motivating** - Doesn't penalize you for days you weren't supposed to study
3. ✅ **Flexible** - Easily adjust schedule if your routine changes
4. ✅ **Consistent** - Maintains same data file as main XP tracker

## Troubleshooting

### "No data file found"
- Make sure `xp_data.json` exists in the same directory
- Run the main XP tracker at least once first

### "Streak still shows as broken"
- The fix updates the JSON file, but doesn't retroactively give back XP
- Your streak number will be corrected going forward
- You can manually edit `xp_data.json` if needed

### "Wrong day showing as study day"
- Check the `STUDY_DAYS` list in `streak_fix.py`
- Remember: 0=Monday, 1=Tuesday, etc.

## Future Enhancements

Potential improvements to consider:
- [ ] Automatic detection of study schedule from calendar
- [ ] Streak freeze days (sick days, holidays)
- [ ] Email/notification reminders for upcoming study days
- [ ] Integration directly into main XP tracker
- [ ] Web dashboard for visualizing streaks

---

**Keep the streak alive! 🔥**

*Remember: Consistency on YOUR schedule is what matters!*
