from django.db import models

# Create your models here.
# daily entry model

# date	DateField (unique per user)
# went_well	TextField
# best_moment	TextField
# learned_today	TextField
# went_bad	TextField
# improve_tomorrow	TextField
# mood	CharField
# created_at	DateTimeField
# updated_at	DateTimeField

class DailyEntryModel(models.Model):
    user = models.ForeignKey(
        "accounts.UserModel",
        on_delete=models.CASCADE,
        related_name="daily_entries",
    )
    date = models.DateField(
        db_column='date',
    )
    went_well = models.TextField(
        db_column='went_well',
    )
    best_moment = models.TextField(
        db_column='best_moment',
    )
    learned_today = models.TextField(
        db_column='learned_today',
    )
    went_bad = models.TextField(
        db_column='went_bad',
    )
    improve_tomorrow = models.TextField(
        db_column='improve_tomorrow',
    )
    mood = models.CharField(
        db_column='mood',
        max_length=50
    )
    created_at = models.DateTimeField(
        db_column='created_at',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        db_column='updated_at',
        auto_now=True
    )

    class Meta:
        db_table = 'daily_entry_model'
        verbose_name = 'Daily Entry'
        verbose_name_plural = 'Daily Entries'

    