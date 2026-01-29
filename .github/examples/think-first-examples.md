# Think-First Examples

## Example 1: Bug Fix

```markdown
## Navrhovaný Plán

Úkol: Fix bug where TM storage doesn't save customer_id

Analýza:
- Bug v backend/app/api/tm_storage.py
- Customer ID not saved when creating TM entry

Přístup:
1. Check TranslationMemory model - má customer_id field?
2. Check create_tm_entry function - passes customer_id?
3. Fix storage logic
4. Add test
5. Test manually

Soubory:
- backend/app/models/database.py - check model
- backend/app/api/tm_storage.py - fix logic
- backend/tests/test_tm_storage.py - add test

Rizika:
- Customer_id může být nullable
- Problém může být v frontendu

Můžu pokračovat?
```

## Example 2: New Feature

```markdown
## Navrhovaný Plán

Úkol: Add customer dropdown to upload modal

Analýza:
- Upload modal v frontend/pages/TMAlignment.tsx
- Potřeba API endpoint pro seznam customerů

Přístup:
1. Create backend API GET /api/v1/customers/dropdown
2. Create frontend service getCustomersDropdown()
3. Add dropdown to modal
4. Add state management
5. Test e2e

Soubory:
- backend/app/api/customers.py - new endpoint
- frontend/services/backendService.ts - service
- frontend/pages/TMAlignment.tsx - UI

Rizika:
- Customers table might not exist
- Dropdown slow with 1000+ customers

Alternativy:
- Autocomplete: Pro: scalable, Con: complex UX
- Existing endpoint: Pro: fast, Con: might not exist

Můžu pokračovat?
```
