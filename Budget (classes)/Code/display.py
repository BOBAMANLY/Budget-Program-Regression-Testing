# Imports

import tkinter as tk
import json
import random
from threading import Thread
from playsound import playsound
import datetime
# import requests

# import winsound
# from tkinter import Grid, ttk
# import webbrowser

class Display:
    def __init__(self):
        """
        Initialize the class
        Inputs: None
        Outputs: None
        """
        # Create Window
        self.window = tk.Tk()

        # Create Title
        self.window.title("Fisher Budget") 

        # Set Window Size
        self.window.geometry("600x600")

        # Configure the rows and columns for grid
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        self.window.columnconfigure(4, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=1)
        self.window.rowconfigure(5, weight=1)
        self.window.rowconfigure(6, weight=1)
        self.window.rowconfigure(7, weight=1)
        self.window.rowconfigure(8, weight=1)
        self.window.rowconfigure(9, weight=1)
        self.window.rowconfigure(10, weight=1)
        self.window.rowconfigure(11, weight=1)
        self.window.rowconfigure(12, weight=1)
        self.window.rowconfigure(13, weight=1)
        self.window.rowconfigure(14, weight=1)
        self.window.rowconfigure(15, weight=1)

        # Initialize the variables
        self.user = ""
        self.portfolio = self.read_info()
        self.exit = False
        self.time_accessed = ""
        self.time_out = ""
        self.system_info = self.read_system_info()
        self.submit_button_exists = True

    def read_system_info(self):
        """
        Open the file and read the data
        Inputs: None
        Outputs: System Info (dictionary)
        """

        with open("Budget (classes)/Files/system_info.json", "r") as file:
            self.system_info = json.load(file)

        # Return the portfolio
        return self.system_info

        # URL for the file to pull
        # url = 'https://raw.githubusercontent.com/BOBAMANLY/Budgeting-Program/main/Budget%20(classes)/Files/system_info.json?token=AWHUSIRGQZZV6X2SEEAQ6VLBYPPKY'
        # response = requests.get(url)

        # # Save the info to the program
        # self.system_info = json.loads(response.text)

    def update_system_info(self):
        """
        Update the system info file
        Inputs: None
        Outputs: None
        """

        # Get start time
        self.get_start_time()
        # Move user info slots in the system info file
        x = 5
        while x > 1:
            self.system_info["User Log-In Records"][str(x)] = self.system_info["User Log-In Records"][str(x - 1)]
            self.system_info["Start Times"][str(x)] = self.system_info["Start Times"][str(x - 1)]
            self.system_info["End Times"][str(x)] = self.system_info["End Times"][str(x - 1)]
            x -= 1
        
        # Add the new user info
        self.system_info["User Log-In Records"]["1"] = self.user
        self.system_info["Start Times"]["1"] = self.time_accessed.strftime("%m/%d/%Y %H:%M:%S")

    def write_system_info(self):
        """
        Write the system info file
        Inputs: None
        Outputs: None
        """

        # Save the system info in the file
        with open("Budget (classes)/Files/system_info.json", "w") as file:
            json.dump(self.system_info, file)

    
    def get_start_time(self):
        self.time_accessed = datetime.datetime.now()
        return self.time_accessed

    def get_end_time(self):
        self.time_out = datetime.datetime.now()
        return self.time_out

    def save_end_time(self):
        """
        Saves the end time
        Inputs: None
        Outputs: None
        """

        # Get the end time
        self.get_end_time()
        # Add the new user info
        self.system_info["End Times"]["1"] = self.time_out.strftime("%m/%d/%Y %H:%M:%S")

    def read_info(self):
        """
        Open the file and read the data
        Inputs: None
        Outputs: portfolio (dictionary)
        """

        with open("Budget (classes)/Files/budget_portfolio.json", "r") as file:
            self.portfolio = json.load(file)

        # Return the portfolio
        return self.portfolio

        # URL for the file to pull
        # url = 'https://raw.githubusercontent.com/BOBAMANLY/Budgeting-Program/main/Budget%20(classes)/Files/budget_portfolio.json?token=AWHUSIWKPXMNADFVDACV5BDBYPPOE'
        # response = requests.get(url)

        # # Save the info to the program
        # self.portfolio = json.loads(response.text)

    def write_info(self):
        """
        Saves the changes to the portfolio
        Inputs: None
        Outputs: None
        """

        with open("Budget (classes)/Files/budget_portfolio.json", "w") as file:
            json.dump(self.portfolio, file)

    def get_user_name(self):
        """
        Identifies the user
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        #label that asks who the user is
        self.label = tk.Label(text="Who is budgeting today?")
        self.label.grid(row=1, column=2)
        #entry box to get users name
        self.button = tk.Button(text="Jacob", command=self._user_jacob)
        self.button.grid(row=3, column=1)
        #button to submit users name
        self.button2 = tk.Button(text="Jaden", command=self._user_jaden)
        self.button2.grid(row=3, column=3)
        self.warning_label = tk.Label(text="Use the Exit buttons to exit the program")
        self.warning_label.grid(row=6, column=2)
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=5, column=2)
        self.window.mainloop()

    def _user_jaden(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.label.destroy()
        self.button.destroy()
        self.button2.destroy()
        self.exit_button.destroy()
        self.warning_label.destroy()
        self.user = "Jaden"

        # Call new action
        self.greeting()

    def _user_jacob(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.label.destroy()
        self.button.destroy()
        self.button2.destroy()
        self.exit_button.destroy()
        self.warning_label.destroy()
        self.user = "Jacob"

        # Call new action
        self.greeting()

    def greeting(self):
        """
        Display the greeting for the user
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        def play_sound():
            """
            Plays the startup sound for Jacob's login
            This is done in a thread
            Inputs: None
            Outputs: Sound
            """

            # Play the entrance sound
            playsound("Budget (classes)\Assets\Jarvis Wise Selection.mp3")

        # Continue
        self.window.title(f"Fisher Budget    User: {self.get_user()}")
        self.g_label = tk.Label(text=f"Hello {self.user}!")
        self.g_label.grid(row=3, column=2)

        # Edit system info
        self.update_system_info()

        if self.user == "Jaden":
            complement_list = ["You are looking great today!"]
            self.label2 = tk.Label(text=random.choice(complement_list))
            self.label2.grid(row=4, column=2)
        elif self.user == "Jacob":
            thread = Thread(target=play_sound)
            thread.daemon = True
            thread.start()
        self.button = tk.Button(text="Main Menu", command=self.main_menu_from_greeting)
        self.button.grid(row=5, column=3)
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=5, column=1)
        self.window.mainloop()
        
    def get_user(self):
        """
        Returns the user
        Inputs: None
        Outputs: user
        """

        if self.user == "Jacob":
            return "Jacob"
        elif self.user == "Jaden":
            return "Jaden"

    def main_menu_from_greeting(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        if self.get_user() == "Jaden":
            self.label2.destroy()
        self.g_label.destroy()
        self.button.destroy()
        self.exit_button.destroy()

        # Call new action
        self.main_menu()

    def main_menu_from_view_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.button.destroy()
        self.bills_button.destroy()
        self.envelopes_button.destroy()
        self.portfolio_button.destroy()
        self.account_balance_button.destroy()
        self.net_button.destroy()
        self.investments_button.destroy()
        self.exit_button.destroy()
        self.main_menu()
        
    def main_menu(self):
        """
        Display the main menu
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.instruction_label = tk.Label(text="What would you like to do?")
        self.instruction_label.grid(row=0, column=2)
        self.pay_button = tk.Button(text="Enter Paycheck", command=self.enter_paycheck_from_main_menu)
        self.pay_button.grid(row=1, column=1)
        self.spend_button = tk.Button(text="Report Spending", command=self.report_spending_from_main_menu)
        self.spend_button.grid(row=2, column=1)
        self.update_button = tk.Button(text="Update Info", command=self.update_info_from_main_menu)
        self.update_button.grid(row=1, column=3)
        self.view_button = tk.Button(text="View Info", command=self.view_info_from_main_menu)
        self.view_button.grid(row=2, column=3)
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=4, column=2)
        self.music_button = tk.Button(text="Play Music", command=self.play_music)
        self.music_button.grid(row=3, column=2)
        self.window.mainloop()

    def report_spending_from_main_menu(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.instruction_label.destroy()
        self.pay_button.destroy()
        self.spend_button.destroy()
        self.update_button.destroy()
        self.view_button.destroy()
        self.exit_button.destroy()
        self.music_button.destroy()

        # Call new action
        self.report_spending()

    def report_spending(self):
        """
        Display the report spending menu
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Return Button
        self.return_button = tk.Button(text="Return", command=self.main_menu_from_report_spending)
        self.return_button.grid(row=0, column=0)

        # Header
        self.header_label = tk.Label(text="Report Spending")
        self.header_label.grid(row=1, column=2)

        # Which User
        self.user_label = tk.Label(text="Which user?")
        self.user_label.grid(row=2, column=1)

        # User menuoptions
        user_options = ["Jacob", "Jaden"]
        self.chosen_user = tk.StringVar()
        self.user_menu = tk.OptionMenu(self.window, self.chosen_user, *user_options)
        self.user_menu.grid(row=2, column=3)

        # category Label
        self.category_label = tk.Label(text="Which category?")
        self.category_label.grid(row=3, column=1)

        # Category Options Menu
        category_options = ["Rent", "Utilities", "Phone", "Insurance", "Groceries", "Deep Savings", "Rainy Day Fund", "Date Night", "Gas", "Tithing", "Play Money"]
        self.chosen_category = tk.StringVar()
        self.category_menu = tk.OptionMenu(self.window, self.chosen_category, *category_options)
        self.category_menu.grid(row=3, column=3)

        # Amount Label
        self.amount_label = tk.Label(text="How much?")
        self.amount_label.grid(row=4, column=1)

        # Amount Entry
        self.amount_entry = tk.Entry()
        self.amount_entry.grid(row=4, column=3)

        # Submit Button
        self.submit_button_exists = True
        self.submit_button = tk.Button(text="Submit")
        self.submit_button.grid(row=5, column=2)

        def expenditure_submission():
            """
            Alter the portfolios based on expenditures
            Inputs: Entries from before
            Outputs: None, Edits open portfolio
            """

            # Get user
            user = self.chosen_user.get().lower()

            # Get category
            category = self.chosen_category.get().lower()

            # Get amount
            amount = float(self.amount_entry.get())

            # Alter portfolio
            if category == "rent":
                self.portfolio["envelope_system"]["rent"] -= amount
            elif category == "utilities":
                self.portfolio["envelope_system"]["utilities"] -= amount
            elif category == "phone bill":
                self.portfolio["envelope_system"]["phone_bill"] -= amount
            elif category == "insurance":
                self.portfolio["envelope_system"]["insurance"] -= amount
            elif category == "play money":
                if user == "jacob":
                    self.portfolio["envelope_system"]["play_money"]["jacob"] -= amount
                elif user == "jaden":
                    self.portfolio["envelope_system"]["play_money"]["jaden"] -= amount
            elif category == "groceries":
                self.portfolio["envelope_system"]["groceries"] -= amount
            elif category == "deep savings":
                self.portfolio["envelope_system"]["deep_savings"] -= amount
            elif category == "rainy day fund": 
                self.portfolio["envelope_system"]["rainy_day_fund"] -= amount
            elif category == "date night":
                self.portfolio["envelope_system"]["date_night"] -= amount
            elif category == "gas":
                self.portfolio["envelope_system"]["gas"] -= amount
            elif category == "tithing":
                if user == "jacob":
                    self.portfolio["envelope_system"]["tithing"]["jacob"] -= amount
                elif user == "jaden":
                    self.portfolio["envelope_system"]["tithing"]["jaden"] -= amount

            # Subtract amount from total account balance
            self.portfolio["account_balances"][user] -= amount

            self.submit_button.destroy()
            self.submit_button_exists = False
        
        self.amount_entry.bind("<KeyRelease>")
        self.submit_button.config(command=expenditure_submission)

    def main_menu_from_report_spending(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.return_button.destroy()
        self.header_label.destroy()
        self.user_label.destroy()
        self.category_label.destroy()
        self.amount_label.destroy()
        self.amount_entry.destroy()
        self.category_menu.destroy()
        self.user_menu.destroy()
        if self.submit_button_exists:
            self.submit_button.destroy()

        # Call new action
        self.main_menu()

    def enter_paycheck_from_main_menu(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.instruction_label.destroy()
        self.pay_button.destroy()
        self.spend_button.destroy()
        self.update_button.destroy()
        self.view_button.destroy()
        self.exit_button.destroy()
        self.music_button.destroy()

        # Call new action
        self.enter_paycheck()

    def enter_paycheck(self):
        """
        Enter a paycheck and alter the portfolio
        Inputs: Paycheck
        Outputs: None
        """

        # Header
        self.paycheck_header_label = tk.Label(text="Enter Paycheck")
        self.paycheck_header_label.grid(row=1, column=2)

        # Return
        self.return_button = tk.Button(text="Return", command=self.main_menu_from_enter_paycheck)
        self.return_button.grid(row=0, column=0)

        # Which User
        self.user_label = tk.Label(text="Which user?")
        self.user_label.grid(row=2, column=1)

        # User menuoptions
        options = ["Jacob", "Jaden"]
        self.chosen_user = tk.StringVar()
        self.user_menu = tk.OptionMenu(self.window, self.chosen_user, *options)
        self.user_menu.grid(row=2, column=3)

        # Paycheck
        self.paycheck_label = tk.Label(text="Paycheck Amount:")
        self.paycheck_label.grid(row=3, column=1)
        self.paycheck_entry = tk.Entry()
        self.paycheck_entry.grid(row=3, column=3)

        # Submit
        self.submit_button = tk.Button(text="Submit")
        self.submit_button.grid(row=4, column=2)

        def income_submission():
            """
            Submit the paycheck
            Inputs: None
            Outputs: None
            """

            # Get paycheck
            paycheck = self.paycheck_entry.get()

            # Get user
            user = self.chosen_user.get().lower()

            # Ensure correct input
            if paycheck == "":
                paycheck = 0.0

            # Alter portfolio
            self.divide_paycheck(user, float(paycheck))

            self.submit_button.destroy()

        self.paycheck_entry.bind("<KeyRelease>")
        self.submit_button.config(command=income_submission)

    def main_menu_from_enter_paycheck(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.paycheck_header_label.destroy()
        self.return_button.destroy()
        self.user_label.destroy()
        self.user_menu.destroy()
        self.paycheck_label.destroy()
        self.paycheck_entry.destroy()
        if self.submit_button_exists:
            self.submit_button.destroy()

        # Call new action
        self.main_menu()
            
    def divide_paycheck(self, user, paycheck):
        """
        Divide the paycheck into the envelopes
        Updates the portfolio
        Inputs: User, paycheck
        Outputs: None
        """

        # Destroy the previous widgets
        self.paycheck_header_label.destroy()
        self.return_button.destroy()
        self.user_label.destroy()
        self.paycheck_label.destroy()
        self.paycheck_entry.destroy()
        self.user_menu.destroy()
        self.submit_button.destroy()

        def help():
            """
            Opens a new window with info on how we normally break up a paycheck
            performs in a thread
            Inputs: None
            Outputs: A new window
            """

            # Create a new window
            help_window = tk.Tk()
            help_window.title("Help")
            help_window.geometry("400x400")

            # Configure grid
            # Columns
            help_window.columnconfigure(0, weight=1)
            help_window.columnconfigure(1, weight=1)
            help_window.columnconfigure(2, weight=1)

            # Rows
            help_window.rowconfigure(0, weight=1)
            help_window.rowconfigure(1, weight=1)
            help_window.rowconfigure(2, weight=1)
            help_window.rowconfigure(3, weight=1)
            help_window.rowconfigure(4, weight=1)
            help_window.rowconfigure(5, weight=1)
            help_window.rowconfigure(6, weight=1)

            # Close window button
            close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
            close_button.grid(row=0, column=0)

            # Help Header
            help_header_label = tk.Label(help_window, text="Normal Paycheck Breakdown")
            help_header_label.grid(row=1, column=1)

            # Tithing Help
            tithing_label = tk.Label(help_window, text="Tithing: 10%")
            tithing_label.grid(row=2, column=1)

            # Rent Help
            rent_label = tk.Label(help_window, text="Rent: 450$")
            rent_label.grid(row=3, column=1)

            # Utilities Help
            utilities_label = tk.Label(help_window, text="Utilities: 50$")
            utilities_label.grid(row=4, column=1)

            # Play Money Help
            play_money_label = tk.Label(help_window, text="Play Money: 20$ (10$ each)")
            play_money_label.grid(row=5, column=1)

            # Extra Help
            extra_label = tk.Label(help_window, text="Put a little in each extra category every time")
            extra_label.grid(row=6, column=1)

        # Help Button
        self.help_button = tk.Button(text="Help", command=help)
        self.help_button.grid(row=0, column=4)

        # User label
        self.user_label = tk.Label(text=f"User: {user}")
        self.user_label.grid(row=1, column=2)

        # Paycheck label
        self.paycheck_label = tk.Label(text=f"Paycheck: ${paycheck}")
        self.paycheck_label.grid(row=1, column=4)

        # Edit the account balances for the user
        self.portfolio["account_balances"][user] += paycheck
        self.account_balance_label = tk.Label(text=f"Account Balance: ${self.portfolio['account_balances'][user]}")
        self.account_balance_label.grid(row=2, column=1)

        # Display the envelopes
        self.rent_envelope_label = tk.Label(text=f"Rent: ${self.portfolio['envelope_system']['rent']}")
        self.rent_envelope_label.grid(row=3, column=1)

        self.utilities_envelope_label = tk.Label(text=f"Utilities: ${self.portfolio['envelope_system']['utilities']}")
        self.utilities_envelope_label.grid(row=4, column=1)

        self.phone_bill_envelope_label = tk.Label(text=f"Phone Bill: ${self.portfolio['envelope_system']['phone_bill']}")
        self.phone_bill_envelope_label.grid(row=5, column=1)

        self.insurance_envelope_label = tk.Label(text=f"Insurance: ${self.portfolio['envelope_system']['insurance']}")
        self.insurance_envelope_label.grid(row=6, column=1)

        self.groceries_envelope_label = tk.Label(text=f"Groceries: ${self.portfolio['envelope_system']['groceries']}")
        self.groceries_envelope_label.grid(row=7, column=1)

        self.deep_savings_envelope_label = tk.Label(text=f"Deep Savings: ${self.portfolio['envelope_system']['deep_savings']}")
        self.deep_savings_envelope_label.grid(row=8, column=1)

        self.rainy_day_fund_envelope_label = tk.Label(text=f"Rainy Day Fund: ${self.portfolio['envelope_system']['rainy_day_fund']}")
        self.rainy_day_fund_envelope_label.grid(row=9, column=1)

        self.date_night_envelope_label = tk.Label(text=f"Date Night: ${self.portfolio['envelope_system']['date_night']}")
        self.date_night_envelope_label.grid(row=10, column=1)

        self.gas_envelope_label = tk.Label(text=f"Gas: ${self.portfolio['envelope_system']['gas']}")
        self.gas_envelope_label.grid(row=11, column=1)

        self.tithing_jacob_envelope_label = tk.Label(text=f"Tithing Jacob: ${self.portfolio['envelope_system']['tithing']['jacob']}")
        self.tithing_jacob_envelope_label.grid(row=12, column=1)

        self.tithing_jaden_envelope_label = tk.Label(text=f"Tithing Jaden: ${self.portfolio['envelope_system']['tithing']['jaden']}")
        self.tithing_jaden_envelope_label.grid(row=13, column=1)

        self.play_money_jacob_envelope_label = tk.Label(text=f"Play Money Jacob: ${self.portfolio['envelope_system']['play_money']['jacob']}")
        self.play_money_jacob_envelope_label.grid(row=14, column=1)

        self.play_money_jaden_envelope_label = tk.Label(text=f"Play Money Jaden: ${self.portfolio['envelope_system']['play_money']['jaden']}")
        self.play_money_jaden_envelope_label.grid(row=15, column=1)

        # Entrys for the envelopes
        self.rent_envelope_entry = tk.Entry()
        self.rent_envelope_entry.grid(row=3, column=3)

        self.utilities_envelope_entry = tk.Entry()
        self.utilities_envelope_entry.grid(row=4, column=3)

        self.phone_bill_envelope_entry = tk.Entry()
        self.phone_bill_envelope_entry.grid(row=5, column=3)

        self.insurance_envelope_entry = tk.Entry()
        self.insurance_envelope_entry.grid(row=6, column=3)

        self.groceries_envelope_entry = tk.Entry()
        self.groceries_envelope_entry.grid(row=7, column=3)

        self.deep_savings_envelope_entry = tk.Entry()
        self.deep_savings_envelope_entry.grid(row=8, column=3)

        self.rainy_day_fund_envelope_entry = tk.Entry()
        self.rainy_day_fund_envelope_entry.grid(row=9, column=3)

        self.date_night_envelope_entry = tk.Entry()
        self.date_night_envelope_entry.grid(row=10, column=3)

        self.gas_envelope_entry = tk.Entry()
        self.gas_envelope_entry.grid(row=11, column=3)

        self.tithing_jacob_envelope_entry = tk.Entry()
        self.tithing_jacob_envelope_entry.grid(row=12, column=3)

        self.tithing_jaden_envelope_entry = tk.Entry()
        self.tithing_jaden_envelope_entry.grid(row=13, column=3)

        self.play_money_jacob_envelope_entry = tk.Entry()
        self.play_money_jacob_envelope_entry.grid(row=14, column=3)

        self.play_money_jaden_envelope_entry = tk.Entry()
        self.play_money_jaden_envelope_entry.grid(row=15, column=3)

        # Submit button
        self.submit_envelopes_button = tk.Button(text="Submit")
        self.submit_envelopes_button.grid(row=0, column=1)

        # TODO: Button on top right that displays amounts for each envelope to enter.

        def envelope_submission():
            """
            Submits the appropriate amount to each envelope
            Inputs: Answers from the entries
            Outputs: Updates portfolio
            """

            # Get the values from the entries
            rent = self.rent_envelope_entry.get()
            utilities = self.utilities_envelope_entry.get()
            phone_bill = self.phone_bill_envelope_entry.get()
            insurance = self.insurance_envelope_entry.get()
            groceries = self.groceries_envelope_entry.get()
            deep_savings = self.deep_savings_envelope_entry.get()
            rainy_day_fund = self.rainy_day_fund_envelope_entry.get()
            date_night = self.date_night_envelope_entry.get()
            gas = self.gas_envelope_entry.get()
            tithing_jacob = self.tithing_jacob_envelope_entry.get()
            tithing_jaden = self.tithing_jaden_envelope_entry.get()
            play_money_jacob = self.play_money_jacob_envelope_entry.get()
            play_money_jaden = self.play_money_jaden_envelope_entry.get()

            # Allow code to continue if some boxes are not filled
            if rent == '':
                rent = self.portfolio['envelope_system']['rent']
            if utilities == '':
                utilities = self.portfolio['envelope_system']['utilities']
            if phone_bill == '':
                phone_bill = self.portfolio['envelope_system']['phone_bill']
            if insurance == '':
                insurance = self.portfolio['envelope_system']['insurance']
            if groceries == '':
                groceries = self.portfolio['envelope_system']['groceries']
            if deep_savings == '':
                deep_savings = self.portfolio['envelope_system']['deep_savings']
            if rainy_day_fund == '':
                rainy_day_fund = self.portfolio['envelope_system']['rainy_day_fund']
            if date_night == '':
                date_night = self.portfolio['envelope_system']['date_night']
            if gas == '':
                gas = self.portfolio['envelope_system']['gas']
            if tithing_jacob == '':
                tithing_jacob = self.portfolio['envelope_system']['tithing']['jacob']
            if tithing_jaden == '':
                tithing_jaden = self.portfolio['envelope_system']['tithing']['jaden']
            if play_money_jacob == '':
                play_money_jacob = self.portfolio['envelope_system']['play_money']['jacob']
            if play_money_jaden == '':
                play_money_jaden = self.portfolio['envelope_system']['play_money']['jaden']

            # Update the portfolio
            self.portfolio['envelope_system']['rent'] += float(rent)
            self.portfolio['envelope_system']['utilities'] += float(utilities)
            self.portfolio['envelope_system']['phone_bill'] += float(phone_bill)
            self.portfolio['envelope_system']['insurance'] += float(insurance)
            self.portfolio['envelope_system']['groceries'] += float(groceries)
            self.portfolio['envelope_system']['deep_savings'] += float(deep_savings)
            self.portfolio['envelope_system']['rainy_day_fund'] += float(rainy_day_fund)
            self.portfolio['envelope_system']['date_night'] += float(date_night)
            self.portfolio['envelope_system']['gas'] += float(gas)
            self.portfolio['envelope_system']['tithing']['jacob'] += float(tithing_jacob)
            self.portfolio['envelope_system']['tithing']['jaden'] += float(tithing_jaden)
            self.portfolio['envelope_system']['play_money']['jacob'] += float(play_money_jacob)
            self.portfolio['envelope_system']['play_money']['jaden'] += float(play_money_jaden)

            # View the portfolio
            self.view_portfolio_from_paycheck_submission()

        #Keybind the entry submission
        self.rent_envelope_entry.bind("<KeyRelease>")
        self.utilities_envelope_entry.bind("<KeyRelease>")
        self.phone_bill_envelope_entry.bind("<KeyRelease>")
        self.insurance_envelope_entry.bind("<KeyRelease>")
        self.groceries_envelope_entry.bind("<KeyRelease>")
        self.deep_savings_envelope_entry.bind("<KeyRelease>")
        self.rainy_day_fund_envelope_entry.bind("<KeyRelease>")
        self.date_night_envelope_entry.bind("<KeyRelease>")
        self.gas_envelope_entry.bind("<KeyRelease>")
        self.tithing_jacob_envelope_entry.bind("<KeyRelease>")
        self.tithing_jaden_envelope_entry.bind("<KeyRelease>")
        self.play_money_jacob_envelope_entry.bind("<KeyRelease>")
        self.play_money_jaden_envelope_entry.bind("<KeyRelease>")

        # Configure the submission button
        self.submit_envelopes_button.config(command=envelope_submission)

    def view_portfolio_from_paycheck_submission(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.user_label.destroy()
        self.paycheck_label.destroy()
        self.account_balance_label.destroy()
        self.rent_envelope_label.destroy()
        self.utilities_envelope_label.destroy()
        self.phone_bill_envelope_label.destroy()
        self.insurance_envelope_label.destroy()
        self.groceries_envelope_label.destroy()
        self.deep_savings_envelope_label.destroy()
        self.rainy_day_fund_envelope_label.destroy()
        self.date_night_envelope_label.destroy()
        self.gas_envelope_label.destroy()
        self.tithing_jacob_envelope_label.destroy()
        self.tithing_jaden_envelope_label.destroy()
        self.play_money_jacob_envelope_label.destroy()
        self.play_money_jaden_envelope_label.destroy()

        self.rent_envelope_entry.destroy()
        self.utilities_envelope_entry.destroy()
        self.phone_bill_envelope_entry.destroy()
        self.insurance_envelope_entry.destroy()
        self.groceries_envelope_entry.destroy()
        self.deep_savings_envelope_entry.destroy()
        self.rainy_day_fund_envelope_entry.destroy()
        self.date_night_envelope_entry.destroy()
        self.gas_envelope_entry.destroy()
        self.tithing_jacob_envelope_entry.destroy()
        self.tithing_jaden_envelope_entry.destroy()
        self.play_money_jacob_envelope_entry.destroy()
        self.play_money_jaden_envelope_entry.destroy()

        self.submit_envelopes_button.destroy()
        self.help_button.destroy()

        # Call the new action
        self.view_portfolio()
        
    def play_music(self):
        """
        Plays the music
        In a thread
        Inputs: None
        Outputs: Plays the music
        """

        def play_songs():
            """
            Plays the music
            Inputs: None
            Outputs: Sound
            """
            if self.user == "Jacob":
                # Initialize variables
                song_order = []
                songs_list = ["Heartless", "Goin Nowhere", "Broadway Girls", "If I Know Me", "Up Down", "The Way I Talk"]
                songs_locations = ["Budget (classes)\Assets\Diplo ft. Morgan Wallen - Heartless.mp3", "Budget (classes)\Assets\Goin' Nowhere (feat. HARDY, Morgan Wallen & Chris Shiflett).mp3", "Budget (classes)\Assets\Lil Durk - Broadway Girls ft Morgan Wallen.mp3", "Budget (classes)\Assets\Morgan Wallen - If I Know Me.mp3", "Budget (classes)\Assets\Morgan Wallen - Up Down feat Florida Georgia Line.mp3", "Budget (classes)\Assets\The Way I Talk - Morgan Wallen.mp3"]
            elif self.user == "Jaden":
                song_order = []
                songs_list = []
                songs_locations = []
            # Loop and create random song order
            x = 0
            while x <= len(songs_list)-1 and self.exit != True:
                index = random.randint(0, len(songs_list)-1)
                while index not in song_order:
                    song_order.append(index)
                    x += 1

            # Play the songs in the created order
            while self.exit != True:
                for number in song_order:
                    playsound(songs_locations[number])

        # Create Thread
        thread = Thread(target=play_songs)

        # Allows thread to end on first cancelation
        thread.daemon = True

        # Start Thread
        thread.start()

    def update_info_from_main_menu(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.instruction_label.destroy()
        self.pay_button.destroy()
        self.spend_button.destroy()
        self.update_button.destroy()
        self.view_button.destroy()
        self.exit_button.destroy()
        if self.user == "Jacob":
            self.music_button.destroy()
        self.update_info()

    def update_info(self):
        """
        Display the update info menu
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.update_label = tk.Label(text="What would you like to update?")
        self.update_label.grid(row=0, column=2)
        self.button = tk.Button(text="Main Menu", command=self.main_menu_from_update_info)
        self.button.grid(row=0, column=0)
        self.bills_button = tk.Button(text="Bills", command=self.bills_from_update_info)
        self.bills_button.grid(row=1, column=1)
        self.investments_button = tk.Button(text="Investments", command=self.investments_from_update_info)
        self.investments_button.grid(row=2, column=1)
        self.accounts_button = tk.Button(text="Accounts", command=self.update_accounts_from_update_info)
        self.accounts_button.grid(row=1, column=3)
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=4, column=2)
        self.window.mainloop()

    def bills_from_update_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.update_label.destroy()
        self.button.destroy()
        self.bills_button.destroy()
        self.investments_button.destroy()
        self.accounts_button.destroy()
        self.exit_button.destroy()
        self.update_bills()

    def update_bills(self):
        """
        Display the update bills menu
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Header
        self.update_header_label = tk.Label(text="Update Bills")
        self.update_header_label.grid(row=1, column=2)

        # Return
        self.return_button = tk.Button(text="Return", command=self.update_info_from_update_bills)
        self.return_button.grid(row=0, column=0)

        # Labels
        # Rent
        self.update_rent_label = tk.Label(text="Rent")
        self.update_rent_label.grid(row=2, column=1)

        # Utilities
        self.update_utilities_label = tk.Label(text="Utilities")
        self.update_utilities_label.grid(row=3, column=1)

        # Phone Bill
        self.update_phone_bill_label = tk.Label(text="Phone Bill")
        self.update_phone_bill_label.grid(row=4, column=1)

        # Insurance
        self.update_insurance_label = tk.Label(text="Insurance")
        self.update_insurance_label.grid(row=5, column=1)

        # Inputs
        # Rent
        self.update_rent_input = tk.Entry()
        self.update_rent_input.grid(row=2, column=3)

        # Utilities
        self.update_utilities_input = tk.Entry()
        self.update_utilities_input.grid(row=3, column=3)

        # Phone Bill
        self.update_phone_bill_input = tk.Entry()
        self.update_phone_bill_input.grid(row=4, column=3)

        # Insurance
        self.update_insurance_input = tk.Entry()
        self.update_insurance_input.grid(row=5, column=3)

        # Submit
        self.submit_button = tk.Button(text="Submit")
        self.submit_button.grid(row=7, column=2)

        def update_bills_submission():
            """
            Update the bills in the database
            Inputs: None
            Outputs: None
            """

            # Get the values from the inputs
            rent = self.update_rent_input.get()
            utilities = self.update_utilities_input.get()
            phone_bill = self.update_phone_bill_input.get()
            insurance = self.update_insurance_input.get()

            # Override empty inputs
            if rent == "":
                rent = self.portfolio["rent"]
            if utilities == "":
                utilities = self.portfolio["utilities"]
            if phone_bill == "":
                phone_bill = self.portfolio["phone_bill"]
            if insurance == "":
                insurance = self.portfolio["insurance"]

            # Update the portfolio
            self.portfolio["rent"] = float(rent)
            self.portfolio["utilities"] = float(utilities)
            self.portfolio["phone_bill"] = float(phone_bill)
            self.portfolio["insurance"] = float(insurance)

        # Keybind the inputs
        self.update_rent_input.bind("<KeyRelease>")
        self.update_utilities_input.bind("<KeyRelease>")
        self.update_phone_bill_input.bind("<KeyRelease>")
        self.update_insurance_input.bind("<KeyRelease>")

        # Configure the submission
        self.submit_button.configure(command=update_bills_submission)

    def update_info_from_update_bills(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.update_header_label.destroy()
        self.return_button.destroy()
        self.update_rent_label.destroy()
        self.update_utilities_label.destroy()
        self.update_phone_bill_label.destroy()
        self.update_insurance_label.destroy()
        self.update_rent_input.destroy()
        self.update_utilities_input.destroy()
        self.update_phone_bill_input.destroy()
        self.update_insurance_input.destroy()
        self.submit_button.destroy()
        self.update_info()

    def investments_from_update_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.update_label.destroy()
        self.button.destroy()
        self.bills_button.destroy()
        self.investments_button.destroy()
        self.accounts_button.destroy()
        self.exit_button.destroy()

        # Call the action
        self.update_investments()

    def update_info_from_update_investments(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.investments_label.destroy()
        self.button.destroy()
        self.jacob_label.destroy()
        self.jaden_label.destroy()
        self.jacob_update_entry.destroy()
        self.jaden_update_entry.destroy()
        self.submit_button.destroy()
        self.update_info()

    def update_investments(self):
        """
        Display the update investments menu
        Inputs: None
        Outputs: Submits information to be changed
        """

        # Return button
        self.button = tk.Button(text="Return", command=self.update_info_from_update_investments)
        self.button.grid(row=0, column=0)

        # Header
        self.investments_label = tk.Label(text="Update Investments")
        self.investments_label.grid(row=0, column=2)

        # Labels
        self.jacob_label = tk.Label(text="Jacob's Investments")
        self.jacob_label.grid(row=1, column=1)
        self.jaden_label = tk.Label(text="Jaden's Investments")
        self.jaden_label.grid(row=2, column=1)

        # Inputs
        self.jacob_update_entry = tk.Entry()
        self.jacob_update_entry.grid(row=1, column=2)
        self.jaden_update_entry = tk.Entry()
        self.jaden_update_entry.grid(row=2, column=2)

        # Submit Button
        self.submit_button = tk.Button(text="Submit")
        self.submit_button.grid(row=3, column=2)

        def submission():
            """
            Submits the information
            Inputs: None (Function uses .get() method to retrive information)
            Outputs: Submits the information
            """

            # Get the inputted information
            jacob_update = self.jacob_update_entry.get()
            jaden_update = self.jaden_update_entry.get()

            # Allow for user error by overriding empty inputs
            if jacob_update == "":
                jacob_update = self.portfolio["investments"]["jacob"]
            if jaden_update == "":
                jaden_update = self.portfolio["investments"]["jaden"]

            # Update the portfolio
            self.portfolio["investments"]["jacob"] = float(jacob_update)
            self.portfolio["investments"]["jaden"] = float(jaden_update)

        # Keybind the entries
        self.jacob_update_entry.bind("<KeyRelease>")
        self.jaden_update_entry.bind("<KeyRelease>")

        # Configure the submit command
        self.submit_button.config(command=submission)

    def update_accounts_from_update_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.update_label.destroy()
        self.button.destroy()
        self.bills_button.destroy()
        self.investments_button.destroy()
        self.accounts_button.destroy()
        self.exit_button.destroy()

        # Call the action
        self.update_accounts()

    def update_accounts(self):
        """
        Display the update accounts menu
        Inputs: None
        Outputs: Submits information to be changed
        """

        # Return button
        self.button = tk.Button(text="Return", command=self.update_info_from_update_accounts)
        self.button.grid(row=0, column=0)

        # Header
        self.accounts_label = tk.Label(text="Update Accounts")
        self.accounts_label.grid(row=1, column=2)

        # Labels
        # Jacob
        self.jacob_checking_label = tk.Label(text="Jacob's Checking")
        self.jacob_checking_label.grid(row=3, column=1)

        # Jaden
        self.jaden_checking_label = tk.Label(text="Jaden's Checking")
        self.jaden_checking_label.grid(row=4, column=1)

        # Inputs
        self.jacob_checking_update_entry = tk.Entry()
        self.jacob_checking_update_entry.grid(row=3, column=3)
        self.jaden_checking_update_entry = tk.Entry()
        self.jaden_checking_update_entry.grid(row=4, column=3)

        # Submit Button
        self.submit_button = tk.Button(text="Submit")
        self.submit_button.grid(row=5, column=2)

        def account_submission():
            """
            Submits the information
            Inputs: None (Function uses .get() method to retrive information)
            Outputs: Submits the information
            """

            # Get the inputted information
            jacob_checking_update = self.jacob_checking_update_entry.get()
            jaden_checking_update = self.jaden_checking_update_entry.get()

            # Allow for user error by overriding empty inputs
            if jacob_checking_update == "":
                jacob_checking_update = self.portfolio["account_balances"]["jacob"]
            if jaden_checking_update == "":
                jaden_checking_update = self.portfolio["account_balances"]["jaden"]

            # Update the portfolio
            self.portfolio["account_balances"]["jacob"] = int(jacob_checking_update)
            self.portfolio["account_balances"]["jaden"] = int(jaden_checking_update)

        # Keybind the entries
        self.jacob_checking_update_entry.bind("<KeyRelease>")
        self.jaden_checking_update_entry.bind("<KeyRelease>")

        # Configure the submit command
        self.submit_button.config(command=account_submission)

    def update_info_from_update_accounts(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.button.destroy()
        self.accounts_label.destroy()
        self.jacob_checking_label.destroy()
        self.jaden_checking_label.destroy()
        self.jacob_checking_update_entry.destroy()
        self.jaden_checking_update_entry.destroy()
        self.submit_button.destroy()

        # Call the action
        self.update_info()

    def main_menu_from_update_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        # Destroy the previous widgets
        self.update_label.destroy()
        self.button.destroy()
        self.bills_button.destroy()
        self.investments_button.destroy()
        self.accounts_button.destroy()
        self.exit_button.destroy()

        # Call the action
        self.main_menu()

    def view_info_from_main_menu(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.instruction_label.destroy()
        self.pay_button.destroy()
        self.spend_button.destroy()
        self.update_button.destroy()
        self.view_button.destroy()
        self.exit_button.destroy()
        if self.user == "Jacob":
            self.music_button.destroy()
        self.view_info()

    def view_info(self):
        """
        Display the view info menu
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.button = tk.Button(text="Main Menu", command=self.main_menu_from_view_info)
        self.button.grid(row=0, column=0)
        self.bills_button = tk.Button(text="View Bills", command=self.view_bills_from_view_info)
        self.bills_button.grid(row=1, column=1)
        self.envelopes_button = tk.Button(text="View Envelopes", command=self.view_envelopes_from_view_info)
        self.envelopes_button.grid(row=1, column=3)
        self.portfolio_button = tk.Button(text="View Portfolio", command=self.view_portfolio_from_view_info)
        self.portfolio_button.grid(row=2, column=1)
        self.account_balance_button = tk.Button(text="View Account Balance", command= self.view_account_balance_from_view_info)
        self.account_balance_button.grid(row=2, column=3)
        self.net_button = tk.Button(text="View Net Worth", command= self.view_net_from_view_info)
        self.net_button.grid(row=3, column=1)
        self.investments_button = tk.Button(text="View Investments", command= self.view_investments_from_view_info)
        self.investments_button.grid(row=3, column=3)
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=4, column=2)
        self.window.mainloop()

    def view_net_from_view_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.button.destroy()
        self.bills_button.destroy()
        self.envelopes_button.destroy()
        self.portfolio_button.destroy()
        self.account_balance_button.destroy()
        self.net_button.destroy()
        self.investments_button.destroy()
        self.exit_button.destroy()
        self.view_net()

    def view_net(self):
        """
        Display the new worth
        Inputs: None
        Outputs: Displays information to user
        """

        # Return Button
        self.return_button = tk.Button(text="Return", command=self.view_info_from_view_net)
        self.return_button.grid(row=0, column=0)

        self.header_label = tk.Label(text="Net Worth")
        self.header_label.grid(row=1, column=2)

        jacob_balance = self.portfolio["account_balances"]["jacob"]
        jaden_balance = self.portfolio["account_balances"]["jaden"]
        jacob_investments = self.portfolio["investments"]["jacob"]
        jaden_investments = self.portfolio["investments"]["jaden"]
        jacob_net = jacob_balance + jacob_investments
        jaden_net = jaden_balance + jaden_investments
        total_net = jacob_net + jaden_net
        self.jacob_net_label = tk.Label(text=f"Jacob's Net Worth: \n{jacob_net:.2f}")
        self.jacob_net_label.grid(row=2, column=1)
        self.jaden_net_label = tk.Label(text=f"Jaden's Net Worth: \n{jaden_net:.2f}")
        self.jaden_net_label.grid(row=2, column=3)
        self.total_net_label = tk.Label(text=f"Total Net Worth: \n{total_net:.2f}")
        self.total_net_label.grid(row=3, column=2)

        # Exit
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=4, column=2)

    def view_info_from_view_net(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.return_button.destroy()
        self.header_label.destroy()
        self.jacob_net_label.destroy()
        self.jaden_net_label.destroy()
        self.total_net_label.destroy()
        self.exit_button.destroy()
        self.view_info()

    def view_investments_from_view_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.button.destroy()
        self.bills_button.destroy()
        self.envelopes_button.destroy()
        self.portfolio_button.destroy()
        self.account_balance_button.destroy()
        self.net_button.destroy()
        self.investments_button.destroy()
        self.exit_button.destroy()
        self.view_investments()

    def view_investments(self):
        """
        Display the investments
        Inputs: None
        Outputs: Displays information to user
        """

        jacob_investments = self.portfolio["investments"]["jacob"]
        jaden_investments = self.portfolio["investments"]["jaden"]

        # Return Button
        self.return_button = tk.Button(text="Return", command=self.view_info_from_view_investments)
        self.return_button.grid(row=0, column=0)

        self.label = tk.Label(text="Investments")
        self.label.grid(row=1, column=2)

        # Jacob Investments
        self.jacob_investments_label = tk.Label(text=f"Jacob's Investments:\n${jacob_investments}")
        self.jacob_investments_label.grid(row=2, column=1)

        # Jaden Investments
        self.jaden_investments_label = tk.Label(text=f"Jaden's Investments:\n${jaden_investments}")
        self.jaden_investments_label.grid(row=2, column=3)

        self.combined_investments_label = tk.Label(text=f"Combined Investments:\n${jacob_investments + jaden_investments:.2f}")
        self.combined_investments_label.grid(row=3, column=2)

        # Exit
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=4, column=2)

        self.window.mainloop()

    def view_info_from_view_investments(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.return_button.destroy()
        self.label.destroy()
        self.jacob_investments_label.destroy()
        self.jaden_investments_label.destroy()
        self.combined_investments_label.destroy()
        self.exit_button.destroy()
        self.view_info()

    def view_account_balance_from_view_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.button.destroy()
        self.bills_button.destroy()
        self.envelopes_button.destroy()
        self.portfolio_button.destroy()
        self.account_balance_button.destroy()
        self.net_button.destroy()
        self.investments_button.destroy()
        self.exit_button.destroy()
        self.view_account_balance()

    def view_account_balance(self):
        """
        Display the account balance
        Inputs: None
        Outputs: Displays information to user
        """

        # Return Button
        self.return_button = tk.Button(text="Return", command=self.view_info_from_account_balance)
        self.return_button.grid(row=0, column=0)

        jacob_balance = self.portfolio["account_balances"]["jacob"]
        jaden_balance = self.portfolio["account_balances"]["jaden"]
        total_account_balance = jacob_balance + jaden_balance
        self.header_label = tk.Label(text="Account Balance")
        self.header_label.grid(row=1, column=2)
        self.label = tk.Label(text=f"Jacob's Account Balance: \n${jacob_balance}")
        self.label.grid(row=2, column=1)
        self.label2 = tk.Label(text=f"Jaden's Account Balance: \n${jaden_balance}")
        self.label2.grid(row=2, column=3)
        self.label3 = tk.Label(text=f"Total Account Balance: \n${total_account_balance}")
        self.label3.grid(row=3, column=2)

        # Exit
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=4, column=2)

        self.window.mainloop()

    def view_info_from_account_balance(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.return_button.destroy()
        self.label.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.header_label.destroy()
        self.exit_button.destroy()
        self.view_info()
        
    def view_portfolio_from_view_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.button.destroy()
        self.bills_button.destroy()
        self.envelopes_button.destroy()
        self.portfolio_button.destroy()
        self.account_balance_button.destroy()
        self.net_button.destroy()
        self.investments_button.destroy()
        self.exit_button.destroy()
        self.view_portfolio()

    def view_portfolio(self):
        """
        Display the portfolio
        Inputs: None
        Outputs: Displays information to user
        """

        # Get info
        jacob_balance = self.portfolio["account_balances"]["jacob"]
        jaden_balance = self.portfolio["account_balances"]["jaden"]
        jacob_investments = self.portfolio["investments"]["jacob"]
        jaden_investments = self.portfolio["investments"]["jaden"]
        rent = self.portfolio["rent"]
        utilities = self.portfolio["utilities"]
        phone_bill = self.portfolio["phone_bill"]
        insurance = self.portfolio["insurance"]
        rent_envelope = self.portfolio["envelope_system"]["rent"]
        utilities_envelope = self.portfolio["envelope_system"]["utilities"]
        phone_bill_envelope = self.portfolio["envelope_system"]["phone_bill"]
        insurance_envelope = self.portfolio["envelope_system"]["insurance"]
        jacob_play_money = self.portfolio["envelope_system"]["play_money"]["jacob"]
        jaden_play_money = self.portfolio["envelope_system"]["play_money"]["jaden"]
        groceries_envelope = self.portfolio["envelope_system"]["groceries"]
        deep_savings_envelope = self.portfolio["envelope_system"]["deep_savings"]
        rainy_day_envelope = self.portfolio["envelope_system"]["rainy_day_fund"]
        date_night_envelope = self.portfolio["envelope_system"]["date_night"]
        gas_envelope = self.portfolio["envelope_system"]["gas"]
        jacob_tithing = self.portfolio["envelope_system"]["tithing"]["jacob"]
        jaden_tithing = self.portfolio["envelope_system"]["tithing"]["jaden"]

        # Return Button
        self.return_button = tk.Button(text="Return", command=self.view_info_from_view_portfolio)
        self.return_button.grid(row=0, column=0)

        # Display Portfolio
        self.label = tk.Label(text="Portfolio")
        self.label.grid(row=1, column=2)

        # Balances
        self.jacob_balance_label = tk.Label(text=f"Jacob's Balance: ${jacob_balance}")
        self.jacob_balance_label.grid(row=2, column=1)
        self.jaden_balance_label = tk.Label(text=f"Jaden's Balance: ${jaden_balance}")
        self.jaden_balance_label.grid(row=2, column=3)

        # Investments
        self.jacob_investments_label = tk.Label(text=f"Jacob's Investments: ${jacob_investments}")
        self.jacob_investments_label.grid(row=3, column=1)
        self.jaden_investments_label = tk.Label(text=f"Jaden's Investments: ${jaden_investments}")
        self.jaden_investments_label.grid(row=3, column=3)

        # Tithing
        self.jacob_tithing_label = tk.Label(text=f"Jacob's Tithing: ${jacob_tithing}")
        self.jacob_tithing_label.grid(row=4, column=1)
        self.jaden_tithing_label = tk.Label(text=f"Jaden's Tithing: ${jaden_tithing}")
        self.jaden_tithing_label.grid(row=4, column=3)

        #Play Money
        self.jacob_play_money_label = tk.Label(text=f"Jacob's Play Money: ${jacob_play_money}")
        self.jacob_play_money_label.grid(row=5, column=1)
        self.jaden_play_money_label = tk.Label(text=f"Jaden's Play Money: ${jaden_play_money}")
        self.jaden_play_money_label.grid(row=5, column=3)

        # Bills
        self.rent_label = tk.Label(text=f"Rent: ${rent}")
        self.rent_label.grid(row=7, column=3)
        self.utilities_label = tk.Label(text=f"Utilities: ${utilities}")
        self.utilities_label.grid(row=8, column=3)
        self.phone_bill_label = tk.Label(text=f"Phone Bill: ${phone_bill}")
        self.phone_bill_label.grid(row=9, column=3)
        self.insurance_label = tk.Label(text=f"Insurance: ${insurance}")
        self.insurance_label.grid(row=10, column=3)

        # Bill Envelopes
        self.rent_envelope_label = tk.Label(text=f"Rent Envelope: ${rent_envelope}")
        self.rent_envelope_label.grid(row=7, column=1)
        self.utilities_envelope_label = tk.Label(text=f"Utilities Envelope: ${utilities_envelope}")
        self.utilities_envelope_label.grid(row=8, column=1)
        self.phone_bill_envelope_label = tk.Label(text=f"Phone Bill Envelope: ${phone_bill_envelope}")
        self.phone_bill_envelope_label.grid(row=9, column=1)
        self.insurance_envelope_label = tk.Label(text=f"Insurance Envelope: ${insurance_envelope}")
        self.insurance_envelope_label.grid(row=10, column=1)

        self.gas_envelope_label = tk.Label(text=f"Gas Envelope: ${gas_envelope}")
        self.gas_envelope_label.grid(row=11, column=3)
        self.groceries_envelope_label = tk.Label(text=f"Groceries Envelope: ${groceries_envelope}")
        self.groceries_envelope_label.grid(row=12, column=3)

        self.deep_savings_envelope_label = tk.Label(text=f"Deep Savings Envelope: ${deep_savings_envelope}")
        self.deep_savings_envelope_label.grid(row=11, column=1)
        self.rainy_day_envelope_label = tk.Label(text=f"Rainy Day Fund Envelope: ${rainy_day_envelope}")
        self.rainy_day_envelope_label.grid(row=12, column=1)
        self.date_night_envelope_label = tk.Label(text=f"Date Night Envelope: ${date_night_envelope}")
        self.date_night_envelope_label.grid(row=13, column=1)

        # Exit
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=14, column=2)
        
        self.window.mainloop()

    def view_info_from_view_portfolio(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.return_button.destroy()
        self.label.destroy()
        self.jacob_balance_label.destroy()
        self.jaden_balance_label.destroy()
        self.jacob_investments_label.destroy()
        self.jaden_investments_label.destroy()
        self.rent_label.destroy()
        self.utilities_label.destroy()
        self.phone_bill_label.destroy()
        self.insurance_label.destroy()
        self.rent_envelope_label.destroy()
        self.utilities_envelope_label.destroy()
        self.phone_bill_envelope_label.destroy()
        self.insurance_envelope_label.destroy()
        self.jacob_play_money_label.destroy()
        self.jaden_play_money_label.destroy()
        self.groceries_envelope_label.destroy()
        self.deep_savings_envelope_label.destroy()
        self.rainy_day_envelope_label.destroy()
        self.date_night_envelope_label.destroy()
        self.gas_envelope_label.destroy()
        self.jacob_tithing_label.destroy()
        self.jaden_tithing_label.destroy()
        self.exit_button.destroy()
        self.view_info()

    def view_envelopes_from_view_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.button.destroy()
        self.bills_button.destroy()
        self.envelopes_button.destroy()
        self.portfolio_button.destroy()
        self.account_balance_button.destroy()
        self.net_button.destroy()
        self.investments_button.destroy()
        self.exit_button.destroy()
        self.view_envelopes()

    def view_envelopes(self):
        """
        Displays all of the envelopes
        Inputs: None
        Outputs: Displays information to the user
        """
        
        rent_envelope = self.portfolio["envelope_system"]["rent"]
        utilities_envelope = self.portfolio["envelope_system"]["utilities"]
        phone_bill_envelope = self.portfolio["envelope_system"]["phone_bill"]
        insurance_envelope = self.portfolio["envelope_system"]["insurance"]
        jacob_play_money = self.portfolio["envelope_system"]["play_money"]["jacob"]
        jaden_play_money = self.portfolio["envelope_system"]["play_money"]["jaden"]
        groceries_envelope = self.portfolio["envelope_system"]["groceries"]
        deep_savings_envelope = self.portfolio["envelope_system"]["deep_savings"]
        rainy_day_envelope = self.portfolio["envelope_system"]["rainy_day_fund"]
        date_night_envelope = self.portfolio["envelope_system"]["date_night"]
        gas_envelope = self.portfolio["envelope_system"]["gas"]
        jacob_tithing = self.portfolio["envelope_system"]["tithing"]["jacob"]
        jaden_tithing = self.portfolio["envelope_system"]["tithing"]["jaden"]
        
        # Return Button
        self.return_button = tk.Button(text="Return", command=self.view_info_from_view_envelopes)
        self.return_button.grid(row=0, column=0)

        self.header_label = tk.Label(text="Envelopes")
        self.header_label.grid(row=1, column=2)

        # Rent Envelope
        self.rent_envelope_label = tk.Label(text=f"Rent Envelope: ${rent_envelope}")
        self.rent_envelope_label.grid(row=5, column=3)

        # Utilities Envelope
        self.utilities_envelope_label = tk.Label(text=f"Utilities Envelope: ${utilities_envelope}")
        self.utilities_envelope_label.grid(row=6, column=3)

        # Phone Bill Envelope
        self.phone_bill_envelope_label = tk.Label(text=f"Phone Bill Envelope: ${phone_bill_envelope}")
        self.phone_bill_envelope_label.grid(row=7, column=3)

        # Insurance Envelope
        self.insurance_envelope_label = tk.Label(text=f"Insurance Envelope: ${insurance_envelope}")
        self.insurance_envelope_label.grid(row=8, column=3)

        # Jacob Play Money
        self.jacob_play_money_label = tk.Label(text=f"Jacob Play Money: ${jacob_play_money}")
        self.jacob_play_money_label.grid(row=2, column=1)

        # Jaden Play Money
        self.jaden_play_money_label = tk.Label(text=f"Jaden Play Money: ${jaden_play_money}")
        self.jaden_play_money_label.grid(row=2, column=3)

        # Groceries Envelope
        self.groceries_envelope_label = tk.Label(text=f"Groceries Envelope: ${groceries_envelope}")
        self.groceries_envelope_label.grid(row=5, column=1)

        # Deep Savings Envelope
        self.deep_savings_envelope_label = tk.Label(text=f"Deep Savings Envelope: ${deep_savings_envelope}")
        self.deep_savings_envelope_label.grid(row=6, column=1)

        # Rainy Day Envelope
        self.rainy_day_envelope_label = tk.Label(text=f"Rainy Day Envelope: ${rainy_day_envelope}")
        self.rainy_day_envelope_label.grid(row=7, column=1)

        # Date Night Envelope
        self.date_night_envelope_label = tk.Label(text=f"Date Night Envelope: ${date_night_envelope}")
        self.date_night_envelope_label.grid(row=8, column=1)

        # Gas Envelope
        self.gas_envelope_label = tk.Label(text=f"Gas Envelope: ${gas_envelope}")
        self.gas_envelope_label.grid(row=9, column=1)

        # Jacob Tithing
        self.jacob_tithing_label = tk.Label(text=f"Jacob Tithing: ${jacob_tithing}")
        self.jacob_tithing_label.grid(row=3, column=1)
        
        # Jaden Tithing
        self.jaden_tithing_label = tk.Label(text=f"Jaden Tithing: ${jaden_tithing}")
        self.jaden_tithing_label.grid(row=3, column=3)

        # Exit
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=10, column=2)

        self.window.mainloop()

    def view_info_from_view_envelopes(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.return_button.destroy()
        self.rent_envelope_label.destroy()
        self.utilities_envelope_label.destroy()
        self.phone_bill_envelope_label.destroy()
        self.insurance_envelope_label.destroy()
        self.jacob_play_money_label.destroy()
        self.jaden_play_money_label.destroy()
        self.groceries_envelope_label.destroy()
        self.deep_savings_envelope_label.destroy()
        self.rainy_day_envelope_label.destroy()
        self.date_night_envelope_label.destroy()
        self.gas_envelope_label.destroy()
        self.jacob_tithing_label.destroy()
        self.jaden_tithing_label.destroy()
        self.header_label.destroy()
        self.exit_button.destroy()
        self.view_info()

    def view_bills_from_view_info(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.button.destroy()
        self.bills_button.destroy()
        self.envelopes_button.destroy()
        self.portfolio_button.destroy()
        self.account_balance_button.destroy()
        self.net_button.destroy()
        self.investments_button.destroy()
        self.exit_button.destroy()
        self.view_bills()

    def view_bills(self):
        """
        Display the bills
        Inputs: None
        Outputs: Information about the bills
        """

        self.return_button = tk.Button(text="Return", command=self.view_info_from_view_bills)
        self.return_button.grid(row=0, column=0)

        self.header_label = tk.Label(text="Bills")
        self.header_label.grid(row=1, column=2)

        # Rent
        rent = self.portfolio["rent"]
        self.rent_label = tk.Label(text=f"Rent: ${rent}")
        self.rent_label.grid(row=2, column=1)

        # Utilities
        utilities = self.portfolio["utilities"]
        self.utilities_label = tk.Label(text=f"Utilities: ${utilities}")
        self.utilities_label.grid(row=3, column=1)

        # Phone
        phone = self.portfolio["phone_bill"]
        self.phone_label = tk.Label(text=f"Phone Bill: ${phone}")
        self.phone_label.grid(row=2, column=3)

        # Insurance
        insurance = self.portfolio["insurance"]
        self.insurance_label = tk.Label(text=f"Insurance: ${insurance}")
        self.insurance_label.grid(row=3, column=3)

        # Exit
        self.exit_button = tk.Button(text="Exit", command=self.leave)
        self.exit_button.grid(row=4, column=2)
        self.window.mainloop()

    def view_info_from_view_bills(self):
        """
        Destroy the previous widgets
        Inputs: None
        Outputs: Directs to the appropriate action
        """

        self.return_button.destroy()
        self.header_label.destroy()
        self.rent_label.destroy()
        self.utilities_label.destroy()
        self.phone_label.destroy()
        self.insurance_label.destroy()
        self.exit_button.destroy()
        self.view_info()

    def leave(self):
        """
        Saves and quits the program.
        Inputs: None
        Outputs: None
        Finished
        """

        self.exit = True

        # Save end time
        self.save_end_time()

        # Save info
        self.write_system_info()
        self.write_info()

        quit()