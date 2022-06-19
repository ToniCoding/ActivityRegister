# ActivityRegister - Short approach.
Activity Register is an app developed in Python which function is an easy registry of an activity done. The program is still under heavy development and most of their functions doesn't work. I'll keep updating it when I have enough time.

# ActivityRegister - Long approach + How does this work?
Basically, AR asks the user for input what wants to do (for now, the only available option is "Create a registry"). The user must use numbers to select an option. In the "main.py" file you can see all the menus which are already stored into a variable.

# ActivityRegister - [FUNCTION] Create registry.
Create registry is the first and the only functional function so far. The process it follows it's simple. Asks the user for an entry title, category and entry.
  - Entry name: Can be assigned any and if it's empty it will assign the default entry name which is "New Entry".
  - Entry category: User can assign any of the ALREADY CREATED CATEGORIES. There are three different categories created: General (Choosen by default and choosen if the category is not created), Physical, Self-care. In the future, user will be able to create, modify and delete categories.
  - Entry: Text of the entry. By default, if the entry is empty the entry will be "emptyEntry".
Once every area is filled, the program will make a summary like this:
"Information about the new registry:
    - Name: entryName
    - Category: category
    - Entry: entryText

Entry will be deprecated in case you input a wrong confirmation.
Are you sure you want to create a new registry with this data? (Y/n): "

Default option is "Y(es)". Then the program creates a XML file which contains the information about the entry and follows the XML schema.

# ActivityRegister - [FUNCTION] Exit.
Ends the program.
  
# ActivityRegister - Checking the registries created.
You can see the registries that have been created in the following path: "./ActivityRegister/registries/xml/regStorage". In the future, you will be able to see the registries directly from the software menu.
  
# ActivityRegister - Registry (XML) file name.
The name of the AR registry follows the following schema: "registry_month_day_THour_Minute_Second". The letter "T" stands for "Time", it's like a highlighter for the time.
