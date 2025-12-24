class ProjectManager:
    def __init__(self):
        self.projects = {}

    def add_project(self, name, housemeister, contact):
        self.projects[name] = {"housemeister":
        housemeister,
                    "contact" : contact,
                    "materials": [],
                    "status": "In Progress"
                    }
        print(f"Project '{name}' added successfully!")

    def add_material(self, project_name, material_list):
        if project_name in self.projects:
            self.projects[project_name] ["materials"].extend(material_list)
            print(f"Materials added to {project_name}.")

        else:
         print("Project not found!")

    def show_summary(self):
        for name, info in self.projects.items():
            print(f"\n--- Project: {name} ---")
            print(f"Manager:  {info['housemeister']} ({info['contact']})")
            print(f"Materials needed: {', '.join(info['materials'])}")
manager = ProjectManager()
manager.add_project("Haspa", "Herr Wolf", "017612345678")
manager.add_material("Steinbohrer", ["Kabel", "Klebesockel"])
manager.show_summary()