class TodoApp:
    def increase_todo(self):
        while True:
            print("\n favour todoApp")
            print("1. increase todo")
            print("2. make i see your todo")
            print("3. you wan put new ones todo")
            print("4. clean the old todo")
            print("#. oya na e go be")

            sub_choice = input("sub-choice").strip()
            if sub_choice == "2":
                todo = input("1 subtodo" \
                "2 todosmall" \
                "3 todobig"
                ": ").strip().lower().capitalize()
            choice = input("Choice: ").strip()

            if choice == "1":
                self.increase_todo()
            elif choice == "2":
                self.make_i_see_your_todo()
            elif choice == "3":
                self.you_wan_put_new_ones_todo()
            elif choice == "4":
                self.clean_old_todo()
            elif choice == "#":
                print("oya na e go be. Byebye!")
                break
            else:
                print("abeg put correct answer, joor.")


    def increase_todo(self):
        todo = input("Todo: ").strip().lower().capitalize()
        if not todo:
            print("abeg put correct answer, joor.")
            return
        self.database.append({"task": todo})
        print("Todo Added..")

    def make_i_see_your_todo(self):
        self.display_items()

    def you_wan_put_new_ones_todo(self):
        if not self.display_items():
            return
        
        user_input = input("put the number wey you wan clean: ").strip()
        if not user_input.isdigit():
            print("add correct number joor!")
            return
            
        edit_no = int(user_input)
        if edit_no < 1 or edit_no > len(self.database):
            print("the number no correct oo")
            return
            
        new_todo = input("Enter new todo: ").strip().capitalize()
        if not new_todo:
            print("abeg put correct answer, joor.")
            return
            
        self.database[edit_no - 1] = {"task": new_todo}
        print("Todo Updated..")

    def clean_old_todo(self):
        if not self.display_items():
            return
            
        user_input = input("Enter the number to delete: ").strip()
        if not user_input.isdigit():
            print("add correct number joor!")
            return
            
        delete_no = int(user_input)
        if delete_no < 1 or delete_no > len(self.database):
            print("add correct number joor")
            return
            
        self.database.pop(delete_no - 1)
        print("oya i don clean am..")

    def run(self):
        while True:
            print("\n favour todoApp")
            print("1. increase todo")
            print("2. make i see your todo")
            print("3. you wan put new ones todo")
            print("4. clean the old todo")
            print("#. oya na e go be")
            
            choice = input("Choice: ").strip()
            
            if choice == "1":
                self.increase_todo()
            elif choice == "2":
                self.make_i_see_your_todo()
            elif choice == "3":
                self.you_wan_put_new_ones_todo()
            elif choice == "4":
                self.clean_old_todo()
            elif choice == "#":
                print("oya na e go be. Byebye!")
                break
            else:
                print("abeg put correct answer, joor.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()