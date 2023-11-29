from faker import Faker
import os
import shutil

fake = Faker("en_UK")


def delete_directory_contents():
    path_originals = "target_directory/originals"
    path_updates = "target_directory/updates"
    path_finals = "target_directory/finals"

    for filename in os.listdir(path_originals):
        file_path = os.path.join(path_originals, filename)

        if os.path.isfile(file_path):
            os.remove(file_path)

    for filename in os.listdir(path_updates):
        file_path = os.path.join(path_updates, filename)

        if os.path.isfile(file_path):
            os.remove(file_path)

    if os.path.exists(path_finals):
        shutil.rmtree(path_finals)

    if os.path.exists(f"target_directory/droplist"):
        os.remove(f"target_directory/droplist")

    if os.path.exists(f"target_directory/allowlist"):
        os.remove(f"target_directory/allowlist")


def create_files(
    number,
    name_seed,
    address_seed,
    location="",
    file_type="",
):
    if location not in ["originals", "updates"]:
        raise ValueError("Invalid location. Use either 'originals' or 'updates'.")

    if name_seed < 0:
        raise ValueError("Seed cannot be empty.")

    names_list = []  # To store the names for droplist or allowlist
    Faker.seed(name_seed)

    for i in range(int(number)):
        random_name = fake.name()
        random_address = fake.address()
        names_list.append(random_name.split(" ")[-1])

        with open(
            f"target_directory/{location}/{random_name.split(' ')[-1]}", "w"
        ) as file:
            file.write(random_name + "\n")

    for i in range(int(number)):
        Faker.seed(address_seed)
        random_address = fake.address()

        with open(f"target_directory/{location}/{names_list[i]}", "a") as file:
            file.write(random_address)

    if file_type == "droplist":
        if os.path.exists(f"target_directory/droplist"):
            os.remove(f"target_directory/droplist")
        with open(f"target_directory/droplist", "a") as file:
            for name in names_list:
                file.write(name + "\n")
    elif file_type == "allowlist":
        if os.path.exists(f"target_directory/allowlist"):
            os.remove(f"target_directory/allowlist")
        with open(f"target_directory/allowlist", "a") as file:
            for name in names_list:
                file.write(name + "\n")
