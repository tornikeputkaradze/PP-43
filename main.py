# -*- coding: utf-8 -*-


from api import GeocodingClient
from models import GeocodingError
from storage import JsonHistoryStorage


def print_menu() -> None:
    print("\n" + "=" * 52)
    print("  გეოკოდირება — ქალაქის სახელიდან კოორდინატები")
    print("=" * 52)
    print("1 — ქალაქის ძებნა")
    print("2 — ისტორიის ნახვა")
    print("3 — ისტორიის გასუფთავება")
    print("0 — გასვლა (ისტორია ავტომატურად შეინახება)")


def ask(prompt: str) -> str:
    return input(prompt).strip()


def main() -> None:
    client = GeocodingClient()
    storage = JsonHistoryStorage()
    history = storage.load()

    print("მოგესალმებით! Open-Meteo Geocoding API.")

    while True:
        print_menu()
        choice = ask("აირჩიეთ: ")

        if choice == "1":
            city = ask("ქალაქის სახელი: ")
            if not city:
                print("შეცდომა: ქალაქის სახელი არ არის შეყვანილი.")
                continue

            count_text = ask("რამდენი შედეგი? (ნაგულისხმევი 1): ")
            try:
                count = int(count_text) if count_text else 1
            except ValueError:
                print("შეცდომა: რაოდენობა უნდა იყოს მთელი რიცხვი.")
                continue

            try:
                results = client.search(city, count=count)
            except (ValueError, GeocodingError) as error:
                print(f"შეცდომა: {error}")
                continue

            for item in results:
                print(f"  ✓ {item}")
                history.append(item)
            storage.save(history)

        elif choice == "2":
            if not history:
                print("ისტორია ცარიელია.")
            else:
                print(f"ისტორია ({len(history)} ჩანაწერი):")
                for index, item in enumerate(history, 1):
                    print(f"  {index}. {item}")

        elif choice == "3":
            history.clear()
            storage.clear()
            print("ისტორია გასუფთავებულია.")

        elif choice == "0":
            storage.save(history)   # დახურვისას ავტომატური შენახვა
            print("ისტორია შენახულია. ნახვამდის!")
            break

        else:
            print("არასწორი არჩევანი. სცადეთ ისევ.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nპროგრამა შეჩერებულია.")
