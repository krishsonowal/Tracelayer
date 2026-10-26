def verify_refund(agent_action, agent_claim, refund_result):
    mismatches = []

    if agent_claim["status"] != refund_result["status"]:
        mismatches.append("Status mismatch")

    if agent_action["order_id"] != refund_result["order_id"]:
        mismatches.append("Order ID mismatch")

    if agent_action["amount"] != refund_result["amount_refunded"]:
        mismatches.append("Refund amount mismatch")

    return mismatches


def main():
    print("Welcome to TraceLayer!")
    print("Our first prototype starts here.")

    cus_dict={}
    cus_orderid=int(input("Enter your order ID: "))
    cus_message=input("Enter your message: ")
    cus_amount=int(input("Enter your refund amount: "))
    cus_dict["order_id"] = cus_orderid
    cus_dict["message"] = cus_message
    cus_dict["amount"] = cus_amount
    
    refund_request = {
        "order_id": "ORD-101",
        "customer_message": "My order arrived damaged. Please refund me.",
        "refund_amount": 499
    }
    print("Refund request:", cus_dict)

    agent_action = {
        "action": "issue_refund",
        "order_id": "ORD-101",
        "amount": 499
    }
    print("Agent action:", agent_action)

    refund_result = {
        "order_id": "ORD-101",
        "amount_refunded": 499,
        "status": "failure"
    }
    print("Actual refund result:", refund_result)

    agent_claim = {
        "status": "success",
        "message": "Refund of 499 completed successfully."
    }
    print("Agent claim:", agent_claim)

    mismatches = verify_refund(
        agent_action, agent_claim, refund_result
    )

    if mismatches:
        print("Verification failed:")
        for mismatch in mismatches:
            print("-", mismatch)
    else:
        print("Verification passed: All fields match.")

if __name__ == "__main__":
    main()