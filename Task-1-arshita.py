# ==========================================
# 🎬 CONTENT CREATOR IDEA VAULT
# Save and Manage Your Content Ideas
# ==========================================

ideas = []

def show_menu():
    print("\n" + "=" * 50)
    print("🎬 CONTENT CREATOR IDEA VAULT")
    print("=" * 50)
    print("1️⃣  Add New Content Idea")
    print("2️⃣  View All Ideas")
    print("3️⃣  Count Total Ideas")
    print("4️⃣  Clear All Ideas")
    print("5️⃣  Exit")
    print("=" * 50)

print("\n🚀 Welcome to Content Creator Idea Vault!")
print("Never lose your creative ideas again.\n")

while True:
    show_menu()

    choice = input("👉 Enter your choice (1-5): ")

    if choice == "1":
        print("\n💡 ADD NEW IDEA")
        idea = input("Enter your content idea: ").strip()

        if idea:
            ideas.append(idea)
            print(f"✅ Idea Added: '{idea}'")
        else:
            print("❌ Idea cannot be empty!")

    elif choice == "2":
        print("\n📚 YOUR SAVED IDEAS")

        if not ideas:
            print("😔 No ideas saved yet.")
        else:
            print("-" * 50)
            for i, idea in enumerate(ideas, start=1):
                print(f"{i}. {idea}")
            print("-" * 50)

    elif choice == "3":
        print("\n📊 IDEA STATISTICS")
        print(f"Total Ideas Saved: {len(ideas)}")

    elif choice == "4":
        if not ideas:
            print("\n⚠️ No ideas to clear.")
        else:
            confirm = input(
                "\nAre you sure you want to delete all ideas? (yes/no): "
            ).lower()

            if confirm == "yes":
                ideas.clear()
                print("🗑️ All ideas deleted successfully!")
            else:
                print("👍 Deletion cancelled.")

    elif choice == "5":
        print("\n🎉 Thank you for using Content Creator Idea Vault!")
        print("Keep creating amazing content! 🚀")
        break

    else:
        print("\n❌ Invalid choice. Please enter a number from 1 to 5.")