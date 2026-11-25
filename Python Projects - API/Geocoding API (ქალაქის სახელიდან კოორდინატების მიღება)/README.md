# 1. Geocoding API — ქალაქის სახელიდან კოორდინატების მიღება

კონსოლური აპლიკაცია, რომელიც იყენებს **Open-Meteo Geocoding API**-ს:

```
GET https://geocoding-api.open-meteo.com/v1/search?name=Tbilisi&count=1&language=ka
```

პასუხი (მაგალითი PDF-დან):

```json
{
  "results": [
    {
      "name": "Tbilisi",
      "latitude": 41.7151,
      "longitude": 44.8271,
      "country": "Georgia"
    }
  ]
}
```

## გაშვება

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

მენიუ: `1` — ძებნა, `2` — ისტორია, `3` — გასუფთავება, `0` — გასვლა.
ძებნის ისტორია ინახება `data/history.json`-ში და ავტომატურად იტვირთება გაშვებისას.

## ფაილები

| ფაილი | დანიშნულება |
| --- | --- |
| `models.py` | `Location` (dataclass), `to_dict`/`from_dict`, საკუთარი exceptions |
| `decorators.py` | `@validate_name`, `@cache`, `@retry(attempts)` |
| `api.py` | `GeocodingClient` — `requests.get` + `params` + `raise_for_status` |
| `storage.py` | `HistoryStorage` (ABC) და `JsonHistoryStorage` — JSON სერიალიზაცია |
| `main.py` | კონსოლური UI (`input()` / `print()`) |

## გამოყენებული თემები (მხოლოდ პრეზენტაციებიდან)

