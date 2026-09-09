# Scripts map

Deze map is bedoeld als vaste opslagstructuur voor scriptdocumentatie en exports.

## Structuur

- `records/` – definitieve script-records in JSON-formaat
- `exports/` – bulk-exporten of ZIP-archieven
- `archive/` – oudere of gearchiveerde records
- `templates/` – sjablonen voor nieuwe script-records

## Aanbevolen standaard

Gebruik JSON als hoofdformaat voor elk script-record, zodat metadata, code, notities en klantinformatie samen bewaard blijven.

## Voorbeeld

Een script-record kan bestaan uit:
- metadata JSON
- SQL of TypeScript codebestand
- HTML/TXT notities
- ZIP export voor delen met collega's

## Richtlijn

Houd records en exports apart. Zo blijft de map schaalbaar als er meer scripts bijkomen.
