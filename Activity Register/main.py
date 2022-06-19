# Imports.
import os
import sys
import platform
import time
import dataParser

# Menus.
# ============================================================================================================ MAIN MENU
mainMenu = '''
    --- MAIN MENU ---\n
[1] - Create registry.\n
[2] - Create category.\n
[3] - See registries and categories.\n
[3] - Settings.\n
[4] - Exit.
'''

# ============================================================================================================ SETTINGS MENU

settingsMenu = '''
    --- SETTINGS MENU ---
[1] - Project information - Prints all the information about this projects and follows the question route.\n
[2] - Defaults configuration - Configure default answers to confirmations.\n
[3] - Registry options - Enter registry options menu selection.\n
[4] - Restore defaults - Restore all settings by defaults.\n
[5] - Factory reset - Delete ALL data, settings, categories and registries (WARNING).\n
[5] - Exit.
'''

# ============================================================================================================ REGISTRY MENU

registryMenu = '''
    --- REGISTRY OPTIONS MENU ---\n
[1] - Delete registry/registries.\n
[2] - Delete category/categories.\n
[3] - Delete all registries.\n
[4] - Delete all categories.\n
[5] - Exit.
'''
# ============================================================================================================ DEFAULTS MENU

defaultsMenu = '''
    --- DEFAULTS MENU ---\n
[1] - Confirmation on keep writing data entries. Default is: {defaultSetting(BOOL)} (True)\n
[2] - Number of confirmations on restore defaults. Default is: {defaultSetting(INT)} (2)\n
[3] - Number of confirmations on factory reset. Default is: {defaultSetting(INT)} (3)\n
[4] - Exit.
'''

# ============================================================================================================ PROJECT MENU

projectMenu = '''
    --- PROJECT MENU ---\n
[1] - Print. Prints project information on screen.\n
[2] - Print and create query. Prints project information on screen and create a file with query information.\n
'''

# ============================================================================================================

# Important variables.
running = True

# Exported lists.
registryAttribs = []

# Categories.
defaultAvailableCategories = ['General', 'Physical', 'Self-care']
availableCategories = []

# File management.
tempStorager = open('./registries/tempStorager/currentEntry.txt', 'r+')

# Functions.
# ============================================================================================================
# This function checks the current OS.
# ============================================================================================================
def systemChecker():
    return sys.platform
# ============================================================================================================

# ============================================================================================================
# This funcion determines the type of clear that needs to be used.
# ============================================================================================================
#def screenClean(systemChecker):
#    systemChecker()
#    if systemChecker() == 'win32':
#        os.system('cls')
#    else:
#        os.system('clear')
# ============================================================================================================

# ============================================================================================================
# This funcion is in charge of re-establish the default values of currentEntry.txt.
# ============================================================================================================
# def defaultCurrentEntryWindows():
#     os.system('cd ./registries/tempStorager')
#     os.system('del currentEntry.txt')
#     os.system('copy currentEntryClear.txt currentEntry.txt')
# ============================================================================================================

# ============================================================================================================
# This function is in charge of having all the information about user's new registry.
# ============================================================================================================
def createRegistry(defaultAvailableCategories, availableCategories, tempStorager): 
    availableCats = defaultAvailableCategories + availableCategories
    totalCategories = ','.join(availableCats)
    try:
        registryName = input('Registry name: ')
        registryName.strip()
        if not registryName:
            print('No registry name provided. Assigning default name New Entry.')
            registryName = 'newEntry'

        category = input(f'Category ({totalCategories}): ')
        if category not in availableCats:
            print('Invalid or non-existent category, assigning default category General.')
            category = 'General'

        entry = input('Type the new entry:\n')
        if not entry:
            entry = 'emptyEntry'

        os.system('cls')
        print(f'''
Information about the new registry:
    >>> Name: {registryName}
    >>> Category: {category}
    >>> Entry: {entry}
    ''')
        
        confirmation = input('Entry will be deprecated in case you input a wrong confirmation.\nAre you sure you want to create a new registry with this data? (Y/n): ')
        if confirmation.lower() == 'y':
            tempStorager.write(f'{registryName} {category} {entry}')
            tempStorager.close()
            dataParser.dataParser()
            print('New entry registered!')
        if confirmation.lower() == 'n':
            print('Entry discarded.')

    except KeyboardInterrupt:
        print('\nCTRL+C. Stopping...')
        running = False
    
    except EOFError:
        print('Entry deprecated')
# ============================================================================================================

# Code.
print('Welcome to Activity Register.\n')

# ============================================================================================================
# Function that conforms the core of the program.
# ============================================================================================================
def main(running):
    while running == True:
        try:
            userChoice = input(f'What do you want to do?\n{mainMenu}')
            os.system('cls')

            if userChoice.isnumeric() == False:
                print('You need to input a number.')
                running = False

            if int(userChoice) == 1:
                createRegistry(defaultAvailableCategories, availableCategories, tempStorager)

            if int(userChoice) == 4:
                confirmation = input('Are you sure? (y/N) ')
                if confirmation.lower() == 'y':
                    running = False
                if not confirmation:
                    continue

        except KeyboardInterrupt:
            print('\nCTRL+C. Stopping...')
            running = False
        
        except ValueError:
            return main(running)
# ============================================================================================================

# Call to the main function.
main(running)