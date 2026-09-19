from skill_weights import SKILL_WEIGHTS


print("----- SKILL WEIGHTS -----")

for skill, weight in SKILL_WEIGHTS.items():

    print(
        f"{skill}: {weight}"
    )