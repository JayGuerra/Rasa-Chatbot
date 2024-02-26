# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
from typing import Any, Text, Dict, List
import httpx


class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # use the tracker to get user data or slots if needed
        account_type = tracker.get_slot('account_type')

        # API Placeholder
        response = requests.get(f"https://api.yourfintech.com/balance/{account_type}")
        balance = response.json().get("balance")

        # Send the message back to the user
        dispatcher.utter_message(text=f"Your {account_type} account balance is ${balance}.")

        return []


class ActionTransferFunds(Action):
    def name(self) -> Text:
        return "action_transfer_funds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract relevant slots or entities
        amount = tracker.get_slot('amount')
        recipient = tracker.get_slot('recipient')

        # logic to transfer funds like calling an API
        # This is a simplified placeholder
        response = "Transfer successful"  # Placeholder response

        dispatcher.utter_message(text=f"Transferred ${amount} to {recipient}. {response}")

        return []


class ActionProvideBudgetingAdvice(Action):
    def name(self) -> Text:
        return "action_provide_budgeting_advice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Static or dynamic budgeting advice could be provided here
        advice = "Consider tracking your spending, setting up a budget, and sticking to it."

        dispatcher.utter_message(text=advice)

        return []
