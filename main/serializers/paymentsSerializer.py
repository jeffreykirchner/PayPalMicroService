from rest_framework import serializers
from main.models import Payments

# class PayementsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payments
#         fields = ['id', 'email', 'amount', 'memo','timestamp']

class PayementsSerializer(serializers.Serializer):
    '''
    serialize REST version of payment model
    '''
    id = serializers.IntegerField(read_only=True)
    
    email = serializers.EmailField(max_length=250)
    amount = serializers.DecimalField(max_digits=5, decimal_places=2)
    memo = serializers.CharField(max_length=250) 
    timestamp = serializers.DateTimeField(format="%m/%d/%Y %H:%M:%S %Z", required=False)
    app = serializers.CharField(required=False)
    note = serializers.CharField(max_length = 250)
    sender_item_id = serializers.CharField(max_length = 250, required=False)

    payout_batch_id_local = serializers.CharField(max_length = 250,default = "", required=False)    #batch payment id locally assinged
    payout_batch_id_paypal = serializers.CharField(max_length = 250,default = "", required=False)   #batch payment id asigned by paypal

    def create(self, validated_data):
        """
        Create and return a new 'Payments' instance, given the validated data.
        """
        return Payments.objects.create(**validated_data)

