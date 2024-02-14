from flask import Blueprint,request
from flask_jwt_extended import jwt_required
from models import db, Payment

payment_bp = Blueprint('payments_bp', __name__)

#  Retrieve a payment
@payment_bp.route('/payments/<int:payment_id>', methods=['GET'])

def get_payment(payment_id):
   payment = Payment.query.get(payment_id)
   if payment:
        return {
            'id': payment.id,
            'payementdate': payment.paymentdate.strftime('%Y-%m-%d'),
            'paymentmethod': payment.paymentmethod,
            'amount': payment.amount
        }
   return 'Payment not found', 404


@payment_bp.route('/payments/<int:payment_id>', methods=['PUT'])

# @jwt_required

def update_payment(payment_id):
   
    payment = Payment.query.get(payment_id)
    if payment:
        data = request.form
        payment.paymentdate = data.get('paymentdate', payment.paymentdate.strftime('%Y-%m-%d'))
        payment.paymentmethod = data.get('paymentmethod', payment.paymentmethod)
        payment.amount = data.get('amount', payment.amount)
        db.session.commit()
        return 'Payment updated successfully!', 200
    return 'Payment not found', 404


# Delete a payment
@payment_bp.route('/payments/<int:payment_id>', methods=['DELETE'])
# @jwt_required
def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        db.session.delete(payment)
        db.session.commit()
        return 'Payment deleted successfully!', 200
    return 'Payment not found', 404




