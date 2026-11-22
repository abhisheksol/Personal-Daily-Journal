from rest_framework import serializers
from journal.models import DailyEntryModel




class DailyEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyEntryModel
        fields = [
            "date",
            "went_well",
            "best_moment",
            "learned_today",
            "went_bad",
            "improve_tomorrow",
            "mood"
            ]

        read_only_fields = ['user']  # user field is read-only, it will be set in the view based on the authenticated user

    def validate(self, data):
        # validate each field to not be empty
        if not data.get('date'):
            raise serializers.ValidationError("Date is required.")
        if not data.get('went_well'):
            raise serializers.ValidationError("Went well is required.")
        if not data.get('best_moment'):
            raise serializers.ValidationError("Best moment is required.")
        if not data.get('learned_today'):
            raise serializers.ValidationError("Learned today is required.")
        if not data.get('went_bad'):
            raise serializers.ValidationError("Went bad is required.")
        if not data.get('improve_tomorrow'):
            raise serializers.ValidationError("Improve tomorrow is required.")
        if not data.get('mood'):
            raise serializers.ValidationError("Mood is required.")

        return data

    def create(self, validated_data):
        daily_entry = DailyEntryModel.objects.create(
            user=validated_data['user'],
            date=validated_data['date'],
            went_well=validated_data['went_well'],
            best_moment=validated_data['best_moment'],
            learned_today=validated_data['learned_today'],
            went_bad=validated_data['went_bad'],
            improve_tomorrow=validated_data['improve_tomorrow'],
            mood=validated_data['mood']
        )
        return daily_entry
