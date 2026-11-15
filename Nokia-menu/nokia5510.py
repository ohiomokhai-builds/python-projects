
#Display a Nokia 5510 Menu from 1-15
#Get number from user through a prompt
#Display choice number menu successful entry
#Display inside menus from choice parent menu when applicable
#Get number from user through prompt
#Display choice inside menu successful entry
#Display invalid output if the required number is not is gotten matched


nokia_menu = """
========== Welcome to the Nokia 5510 Menu =========   

                1. Phone book
                2. Messages
                3. Chat
                4. Call register
                5. Tones
                6. Settings
                7. Call divert
                8. Music
                9. Games
                10. Calculator
                11. Reminders
                12. Clock
                13. Profiles
                14. Services
                15. SIM service

================== ************ ==================== 
"""

print(f"{nokia_menu}\n")
home_menu = input("Enter any choice menu number: \n")

match home_menu:
        case "1": 
            phone_book = """
            ========== Phone Book =========   
                    
                    1. Search
                    2. Service Nos.1
                    3. Add name
                    4. Erase
                    5. Edit
                    6. Copy
                    7. Assign tone
                    8. Send b’card
                    9. Options
                    10. Speed dials
                    11. Voice tags

            =========== ********* =========
            """
            print(f"{phone_book}\n")
            first_menu = input("Enter any choice menu number: \n")
            match first_menu:
                case "1":
                    print("Search\n")
                case "2":
                    print("Service Nos.1\n")
                case "3":
                    print("Add name\n")
                case "4":
                    print("Erase\n")
                case "5":
                    print("Edit\n")
                case "6":
                    print("Copy\n")
                case "7":
                    print("Assign tone\n")
                case "8":
                    print("Send b’card\n")
                case "9":
                    options = """
                    ===== Options Menu ====
                                
                        1. Memory in use
                        2. Type of view
                        3. Memory status
                                
                    ======================== 
                    """
                    print(f"{options}\n")
                    option_menu = input("Enter any choice menu number: \n")
                    match option_menu:
                        case "1":
                            print("Memory in use\n")
                        case "2":
                            print("Type of view\n")
                        case "3":
                            print("Memory Status\n")
                        case "0":
                            print("Returning to the parent menu\n")
                        case _:
                            print("Invalid choice. Please choose correctly\n")
                case "10":
                    print("Speed dials\n")
                case "11": 
                    print("Voice tags\n")
                case _:
                    print("Invalid choice. Check correctly and try again\n") 
        
        case "2":
            message_menu = """
            ===== Message ===============
                  
              1. Write messages
              2. Inbox
              3. Outbox
              4. Picture messages
              5. Templates
              6. Smileys
              7. Message settings
              8. Info service
              9. Voice mailbox number
              10. Service command editor
                  
            ==============================
            """
            print(f"{message_menu}\n")
            second_menu= input("Enter any choice menu number: \n")
            match second_menu:
                case "1":
                    print("Memory Status\n")
                case "2": 
                    print("Inbox\n")
                case "3":
                    print("Outbox\n")
                case "4":
                    print("Picture messages\n")
                case "5":
                    print("Templates\n")
                case "6":
                    print("Smileys\n")
                case "7":
                    message_settings = """    
                     ===== Message Settings Menu ====
                                
                                1. Set1
                                2. Common
                                
                    =================================
                    """
                    print(f"{message_settings}\n")
                    menu_7 = input("Enter any choice menu number: \n")
                    match menu_7:
                        case "1":
                            set_one = """
                            ===== Set1 Menu ========
                                    
                            1. Message center number
                            2. Messages sent as
                            3. Message validity
                                    
                            ========================
                            """
                            print(f"{set_one}\n")
                            menu_set = input("Enter any choice menu number: \n")
                            match menu_set:
                                case "1":
                                    print("Message center number\n")
                                case "2":
                                    print("Messages sent as\n")
                                case "3":
                                    print("Message validity\n")
                                case _:
                                    print("Invalid choice. Check correctly and try again\n")     
                        case "2":
                            common = """
                            ===== Common Menu ======
                                  
                            1. Delivery reports
                            2. Reply via same centre
                            3. Character support
                                  
                            ========================
                            """
                            print(f"{common}\n")
                            common_menu = input("Enter any choice menu number: \n")
                            match common_menu:
                                case "1":
                                    print("Delivery reports\n")
                                case "2":
                                    print("Reply via same centre\n")
                                case "3":
                                    print("Character support\n")
                              # case 0:
                               #     print("Returning to previous menu∖n")
                                case _:
                                    print("Invalid choice. Please, try again!!\n")                            
                case "8": 
                    print("Info service\n")
                case "9": 
                    print("Voice mailbox number\n")
                case "10": 
                    print("Service command editor\n")
                case _:
                    print("Invalid choice. Check correctly and try again\n") 
            
        case "3":
            print("Chat\n")
        
        case "4":
            call_register = """
            ===== Call Register Menu ====
              
              1. Missed calls
              2. Received calls
              3. Dialed numbers
              4. Erase recent call lists
              5. Show call duration
              6. Show call costs
              7. Call cost settings
              8. Prepaid credit
              
            ===============================
            """
            print(f"{call_register}\n")
            call_register_menu = input("Enter any choice menu number: \n")
            match call_register_menu:
                case "1":
                    print("Missed calls\n")
                case "2":
                    print("Received calls\n")
                case "3":
                    print("Dialed numbers\n")
                case "4":
                    print("Erase recent call lists\n")
                case "5":
                    call_duration = """
                    ===== Show Costs Menu ====
                        
                        1. Last call duration
                        2. All calls’ duration
                        3. Received calls’ duration
                        4. Dialed calls’ duration
                        5. Clear timers
                            
                    ===========================
                    """
                    print(f"{call_duration}\n")
                    call_duration_menu = input("Enter any choice menu number: \n")
                    match call_duration_menu:
                        case "1":
                            print("Last call duration\n")
                        case "2":
                            print("All calls' duration\n")
                        case "3":
                            print("Received calls' duration\n")
                        case "4":
                            print("Dialed calls' duration\n")
                        case "5":
                            print("Clear timers\n")
                        case _:
                            print("Invalid choice. Check correctly and try again\n") 
                case "6": 
                    show_costs = """
                    ===== Show Costs Menu ====
                    
                        1. Last call cost
                        2. All calls’ cost
                        3. Clear counters
                    
                    ============================
                    """
                    print(f"{show_costs}\n")
                    show_costs_menu = input("Enter any choice menu number: \n")
                    match show_costs_menu:
                        case "1":
                            print("Last call cost\n")
                        case "2":
                            print("All calls' cost\n")
                        case "3":
                            print("Clear counters\n")
                        case _:
                            print("Invalid choice. Check correctly and try again\n") 
                case "7":
                    call_costs = """
                    ===== Call cost settings ====
                    
                        1. Call cost limit
                        2. Show costs in
                       
                    =============================
                    """
                    print(f"{call_costs}\n")
                    call_costs_menu = input("Enter any choice menu number: \n")
                    match call_costs_menu:
                        case "1":
                            print("Call cost limit\n")
                        case "2":
                            print("Show costs in\n")
                        case _:
                            print("Invalid choice. Check correctly and try again\n") 
                case "8":
                    print("Prepaid credit\n")
                case _:
                    print("Invalid choice. Check correctly and try again\n") 
            
        case "5":
            tones = """
            ===== Tones Menu ===========
                  
                  1. Ringing tone
                  2. Ringing volume
                  3. Incoming call alert
                  4. Message alert tone
                  5. Keypad tones
                  6. Warning tones
                  7. Vibrating alert
                  8. Screen saver
                  
            =============================
            """
            print(f"{tones}\n")
            tones_menu = input("Enter any choice menu number: \n")
            match tones_menu:
                case "1":
                    print("Ringing tone\n")
                case "2":
                    print("Ringing volume\n")
                case "3":
                    print("Incoming call alert\n")
                case "4":
                    print("Message alert tone\n")
                case "5":
                    print("Keypad tones\n")
                case "6":
                    print("Warning tones\n")
                case "7":
                    print("Vibrating alert\n")
                case "8":
                    print("Screen saver\n")
                case _:
                    print("Invalid choice. Check correctly and try again\n") 
        
        case "6":
            settings = """
            ===== Settings Menu =========
                  
              1. Call settings
              2. Phone settings
              3. Security level
              4. Restore factory settings
                
            ==============================
            """
            print(f"{settings}\n")
            settings_menu = input("Enter any choice menu number: \n")
            match settings_menu:
                case "1":
                    call_settings = """
                    ===== Call Settings Menu =====
                        
                        1. Automatic redial
                        2. Speed dialing
                        3. Call waiting options
                        4. Own number sending
                        5. Phone line in use
                        6. Automatic answer
                      
                    ===============================
                    """
                    print(f"{call_settings}\n")
                    call_settings_menu = input("Enter any choice menu number: \n")
                    match call_settings_menu:
                        case "1":
                            print("Automatic redial\n")
                        case "2":
                            print("Speed dialing\n")
                        case "3":
                            print("Call waiting options\n")
                        case "4":
                            print("Own number sending\n")
                        case "5":
                            print("Phone line in use\n")
                        case "6":
                            print("Automatic answer\n")
                        case _:
                            print("Invalid choice. Check correctly and try again\n") 
                case "2":
                    phone_settings = """
                    ===== Phone Settings Menu ====
                        
                    1. Language
                    2. Cell info display
                    3. Welcome note
                    4. Network selection
                    5. Confirm SIM service actions
                                              
                    ==============================
                    """
                    print(f"{phone_settings}\n")
                    phone_settings_menu = input("Enter any choice menu number: \n")
                    match phone_settings_menu:
                        case "1":
                            print("Language\n")
                        case "2":
                            print("Cell info display\n")
                        case "3":
                            print("Welcome note\n")
                        case "4":
                            print("Network selection\n")
                        case "5":
                            print("Confirm SIM service actions\n")
                        case _:
                            print("Invalid choice. Check correctly and try again\n") 
                case "3":
                    security_settings = """
                    ===== Security Settings Menu ====
                        
                          1. PIN code request
                          2. Call barring service
                          3. Fixed dialing
                          4. Closed user group
                          5. Security level
                          6. Change access codes
                          
                    =================================
                    """
                    print(f"{security_settings}\n")
                    security_settings_menu = input("Enter any choice menu number: \n")
                    match security_settings_menu:
                        case "1":
                            print("PIN code request\n")
                        case "2":
                            print("Call barring service\n")
                        case "3":
                            print("Fixed dialing\n")
                        case "4":
                            print("Closed user group\n")
                        case "5":
                            print("Security level\n")
                        case "6":
                            print("Change access codes\n")
                        case _:
                            print("Invalid choice. Check correctly and try again\n") 
                case "4":
                    print("Restore factory settings\n")
                case _:
                    print("Invalid choice. Check correctly and try again\n") 
            
        case "7":
            print("Call divert\n")
        
        case "8":
            music = """
            ===== Music Menu ====
                  
                1. Music player
                2. Radio
                3. Recorder
                4. Track list
                  
            ======================
            """
            print(f"{music}\n")
            music_menu = input("Enter any choice menu number: \n")
            match music_menu:
                case "1":
                    print("Music player\n")
                case "2":
                    print("Radio\n")
                case "3":
                    print("Recorder\n")
                case "4":
                    print("Track list\n")
                case _:
                    print("Invalid choice. Choose correctly!\n")
            
        case "9":
            print("Games\n")
        
        case "10":
            print("Calculator\n")
        
        case "11":
            print("Reminders\n")
        
        case "12":
            clock = """
            ===== Clock =======================
                        
              1. Alarm clock
              2. Clock settings
              3. Date setting
              4. Stopwatch
              5. Countdown timer
              6. Auto update of date and time
                                                    
            ===================================
            """
            print(f"{clock}\n")
            clock_menu = input("Enter any choice menu number: \n")
            match clock_menu:
                case "1":
                    print("Alarm clock\n")
                case "2":
                    print("Clock settings\n")
                case "3":
                    print("Date setting\n")
                case "4":
                    print("Stopwatch\n")
                case "5":
                    print("Countdown timer\n")
                case "6":
                    print("Auto update of date and time\n")
                case _:
                    print("Invalid choice. Choose correctly!!\n") 
                
        case "13":
            print("Profiles\n")
        
        case "14":
            print("Service\n")
        
        case "15" :
            print("SIM services\n")
        
        case _:
            print("Invalid choice. Choose correctly!!\n")


#End of Nokia Menu Map
