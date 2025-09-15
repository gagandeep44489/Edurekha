

## POST /api/wallet/withdraw
Request JSON: { "user_id": "string", "amount": 10.00 }
Response JSON: { "status": "success", "transaction_id": "tx_5678", "balance": 1090.50 }


# Error structure
{ "status": "error", "code": 400, "message": "insufficient funds" }