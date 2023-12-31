__author__ = "Kirsten Ardolf"
__date__ = "Oct 24, 2023"

from typing import Dict


def determine_contestant_location(city: str) -> str:
    municipality: Dict[str, Dict[str, int]] = {
        "Reykjavik": {"Reykjavik": 0, "Akureyri": 388} ,
        "Kopavogur": {"Reykjavik": 6, "Akureyri": 387} ,
        "Hafnarfjordur": {"Reykjavik": 12 , "Akureyri": 391} ,
        "Reykjanesbaer": {"Reykjavik": 48, "Akureyri": 427} ,
        "Akureyri": {"Reykjavik": 388 , "Akureyri": 0} ,
        "Gardabaer": {"Reykjavik": 9, "Akureyri": 389} ,
        "Mosfellsbaer": {"Reykjavik": 16, "Akureyri": 371} ,
        "Arborg": {"Reykjavik": 64, "Akureyri": 428} ,
        "Akranes": {"Reykjavik": 49, "Akureyri": 350} ,
        "Fjardabyggd": {"Reykjavik": 659 , "Akureyri": 290} ,
        "Mulathing": {"Reykjavik": 603 , "Akureyri": 216} ,
        "Seltjarnarnes": {"Reykjavik": 4, "Akureyri": 390}
    }
    if city in municipality:
        if municipality[city]["Reykjavik"] < municipality[city]["Akureyri"]:
            return "Reykjavik"
        elif municipality[city]["Reykjavik"] > municipality[city]["Akureyri"]:
            return "Akureyri"
    return "str"


def main() -> None:
    city = input()
    output = determine_contestant_location(city)
    print(output)


if __name__ == "__main__":
    main()
