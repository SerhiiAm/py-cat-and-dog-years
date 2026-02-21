def get_human_age(cat_age: int, dog_age: int) -> list:

    def calculate_single_age(animal_age: int, year_step: int) -> int:

        if animal_age < 15:
            return 0

        human_years = 1

        if animal_age >= 24:
            human_years += 1

            extra_years = (animal_age - 24) // year_step
            human_years += extra_years

        return human_years

    return [
        calculate_single_age(cat_age, 4),  # Cat step is 4 (Шаг кота — 4)
        calculate_single_age(dog_age, 5)  # Dog step is 5 (Шаг собаки — 5)
    ]
