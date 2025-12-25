import json

class ProjectManager:
    def __init__(self):
        try:
            with open("data.json", "r") as f:
                self.projects = json.load(f)
        except:
                        self.projects = {}
    def save(self):
            with open("data.json", "w") as f:
                    json.dump(self.projects, f, indent=4)
    def add_project(self, name, caretaker, contact):
            self.projects[name] = {"caretaker": caretaker,
                                                            "contact": contact,
                                                            "materials": [],
                                                            "status": "In Progress"
                                                            }
            self.save()
            print(f"project '{name}' added and saved!")
    def add_material(self, project_name, material_list):
            if project_name in self.projects:
                          self.projects[project_name] ["materials"].extend(material_list)
                          self.save()
                          print(f"Materials updated for {project_name}.")
            else:
                        print("Project not found!")
    def show_summary(self):
            if not self.projects:
                print("No projects found.")
            for name, info in self.projects.items():
                        print(f"\n-- Project: {name} ---")
                        print(f"Manager: {info['caretaker']} ({info['contact']})")
                        print(f"Materials: {', '.join(info['materials'])}")
if __name__ == "__main__":
    manager = ProjectManager()
    manager.show_summary()         

if __name__ == "__main__":
 manager.add_project("Haspa_Test", "Herr Kleider", "017612345678")
 manager.add_material("Haspa_Test", ["Steinbohrer 6mm", "Klebesockel"])