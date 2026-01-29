# Testing Examples

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Overview

Detailed test examples for [testing-protocol.md](../core/testing-protocol.md)

---

## 🐛 Regression Test Examples {#regression}

### Example 1: Merged Cell Duplication Bug

**Bug:** Parser duplicates merged cell content

**Regression Test (BEFORE fix):**
```python
# backend/tests/unit/test_document_parser.py

def test_merged_cells_not_duplicated():
    """Regression test for merged cell duplication bug."""
    # Arrange
    document = create_test_document_with_merged_cells()
    parser = DocumentParser()
    
    # Act
    result = parser.parse(document)
    
    # Assert
    assert len(result.cells) == 3  # Not 6 (duplicated)
    assert result.cells[0].value == "Merged Content"
    assert result.cells[1].value == "Cell 2"
    assert result.cells[2].value == "Cell 3"
```

**Result (BEFORE fix):**
```
FAILED - Expected 3 cells, got 6
```

**After fix:**
```
PASSED - Merged cells no longer duplicated
```

**Commit:**
```bash
git commit -m "fix(parser): resolve merged cell duplication (2026-01-23 14:30 CET)

- Add regression test (proves bug)
- Skip already processed merged cells
- Test now passes"
```

---

### Example 2: Date Parsing Edge Case

**Bug:** Date parser fails on Czech date format

**Regression Test:**
```python
def test_czech_date_format_parsing():
    """Regression: Czech dates should parse correctly."""
    # Arrange
    parser = DateParser()
    czech_date = "23. ledna 2026"
    
    # Act
    result = parser.parse(czech_date)
    
    # Assert
    assert result.year == 2026
    assert result.month == 1
    assert result.day == 23
```

---

## ✨ New Feature Test Examples {#new-feature}

### Example 1: Legal Domains API Endpoint

**Feature:** Add GET /api/v1/legal-domains

**Integration Test:**
```python
# backend/tests/integration/test_legal_domains.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestLegalDomainsEndpoint:
    """Tests for GET /api/v1/legal-domains endpoint."""
    
    def test_get_legal_domains_success(self):
        """Happy path: Return legal domains with valid query."""
        # Arrange
        query = "občanské právo"
        
        # Act
        response = client.get(
            "/api/v1/legal-domains",
            params={"query": query}
        )
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "results" in data
        assert len(data["results"]) > 0
        assert data["results"][0]["name"] == "Občanské právo"
    
    def test_get_legal_domains_empty_query(self):
        """Edge case: Empty query returns all domains."""
        # Act
        response = client.get("/api/v1/legal-domains")
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert len(data["results"]) > 0
    
    def test_get_legal_domains_no_match(self):
        """Edge case: No matching domains."""
        # Act
        response = client.get(
            "/api/v1/legal-domains",
            params={"query": "nonexistent"}
        )
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["results"] == []
    
    def test_get_legal_domains_invalid_param(self):
        """Error handling: Invalid parameter."""
        # Act
        response = client.get(
            "/api/v1/legal-domains",
            params={"invalid": "param"}
        )
        
        # Assert
        assert response.status_code == 422  # Validation error
```

**Unit Test (Service Layer):**
```python
# backend/tests/unit/test_legal_domains_service.py

from app.services.legal_domains_service import LegalDomainsService

class TestLegalDomainsService:
    
    def test_search_legal_domains_exact_match(self):
        """Service returns exact matches first."""
        # Arrange
        service = LegalDomainsService()
        
        # Act
        results = service.search("Občanské právo")
        
        # Assert
        assert len(results) > 0
        assert results[0].name == "Občanské právo"
    
    def test_search_legal_domains_partial_match(self):
        """Service returns partial matches."""
        # Arrange
        service = LegalDomainsService()
        
        # Act
        results = service.search("občan")
        
        # Assert
        assert len(results) > 0
        assert any("občan" in r.name.lower() for r in results)
    
    def test_search_legal_domains_caching(self):
        """Service caches results."""
        # Arrange
        service = LegalDomainsService()
        query = "trestní právo"
        
        # Act
        results1 = service.search(query)
        results2 = service.search(query)  # Should hit cache
        
        # Assert
        assert results1 == results2
        assert service._cache_hits > 0
```

---

### Example 2: File Upload Feature

**Feature:** Upload and process Excel files

**Integration Test:**
```python
def test_upload_valid_excel_file():
    """Upload valid Excel file and process."""
    # Arrange
    test_file = create_test_excel()
    
    # Act
    response = client.post(
        "/api/v1/upload",
        files={"file": ("test.xlsx", test_file, "application/vnd.ms-excel")}
    )
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "file_id" in data

def test_upload_invalid_file_type():
    """Reject non-Excel files."""
    # Arrange
    test_file = create_test_pdf()
    
    # Act
    response = client.post(
        "/api/v1/upload",
        files={"file": ("test.pdf", test_file, "application/pdf")}
    )
    
    # Assert
    assert response.status_code == 400
    assert "Invalid file type" in response.json()["detail"]

def test_upload_corrupted_file():
    """Handle corrupted Excel files gracefully."""
    # Arrange
    corrupted_file = b"corrupted data"
    
    # Act
    response = client.post(
        "/api/v1/upload",
        files={"file": ("test.xlsx", corrupted_file, "application/vnd.ms-excel")}
    )
    
    # Assert
    assert response.status_code == 422
    assert "Unable to process file" in response.json()["detail"]
```

---

## 🧪 Unit Test Examples

### Example 1: Date Validation Logic

```python
from app.utils.validators import validate_date

def test_validate_date_valid_format():
    """Valid date string passes validation."""
    assert validate_date("2026-01-23") is True

def test_validate_date_invalid_format():
    """Invalid format raises ValueError."""
    with pytest.raises(ValueError, match="Invalid date format"):
        validate_date("23-01-2026")

def test_validate_date_future_date():
    """Future dates are allowed."""
    assert validate_date("2030-12-31") is True

def test_validate_date_none():
    """None value raises TypeError."""
    with pytest.raises(TypeError):
        validate_date(None)
```

---

### Example 2: Text Processing

```python
from app.services.text_processor import normalize_text

def test_normalize_text_removes_extra_spaces():
    """Normalize removes multiple spaces."""
    assert normalize_text("Hello  world") == "Hello world"

def test_normalize_text_lowercase():
    """Normalize converts to lowercase."""
    assert normalize_text("HELLO") == "hello"

def test_normalize_text_czech_characters():
    """Normalize preserves Czech characters."""
    assert normalize_text("Občanské právo") == "občanské právo"

def test_normalize_text_empty_string():
    """Empty string returns empty."""
    assert normalize_text("") == ""
```

---

## 🎭 End-to-End Test Examples

### Example 1: Complete User Journey (Playwright)

```typescript
// tests/e2e/legal-domains-search.spec.ts

import { test, expect } from '@playwright/test';

test.describe('Legal Domains Search', () => {
  
  test('User can search and view legal domains', async ({ page }) => {
    // Navigate to app
    await page.goto('http://localhost:3000');
    
    // Search for legal domain
    await page.fill('[data-testid="search-input"]', 'občanské právo');
    await page.click('[data-testid="search-button"]');
    
    // Wait for results
    await page.waitForSelector('[data-testid="search-results"]');
    
    // Verify results
    const results = await page.locator('[data-testid="result-item"]');
    await expect(results).toHaveCount(1);
    await expect(results.first()).toContainText('Občanské právo');
    
    // Click first result
    await results.first().click();
    
    // Verify detail page
    await expect(page.locator('h1')).toContainText('Občanské právo');
  });
  
  test('User sees error message for no results', async ({ page }) => {
    await page.goto('http://localhost:3000');
    
    await page.fill('[data-testid="search-input"]', 'nonexistent');
    await page.click('[data-testid="search-button"]');
    
    await expect(page.locator('[data-testid="no-results"]'))
      .toContainText('No results found');
  });
});
```

---

## ⚡ Performance Test Examples

### Example 1: API Response Time

```python
# tests/performance/test_api_performance.py

import pytest
import time

def test_legal_domains_endpoint_performance():
    """Legal domains endpoint responds within 200ms."""
    # Arrange
    iterations = 100
    response_times = []
    
    # Act
    for _ in range(iterations):
        start = time.time()
        response = client.get("/api/v1/legal-domains", params={"query": "občanské"})
        end = time.time()
        
        assert response.status_code == 200
        response_times.append((end - start) * 1000)  # Convert to ms
    
    # Assert
    avg_response_time = sum(response_times) / len(response_times)
    assert avg_response_time < 200, f"Avg response time: {avg_response_time}ms"
    
    # 95th percentile
    p95 = sorted(response_times)[int(0.95 * len(response_times))]
    assert p95 < 300, f"95th percentile: {p95}ms"
```

### Example 2: Database Query Performance

```python
def test_legal_domains_query_performance(benchmark):
    """Legal domains query executes in < 50ms."""
    from app.services.legal_domains_service import LegalDomainsService
    
    service = LegalDomainsService()
    
    # Benchmark the query
    result = benchmark(service.search, "občanské právo")
    
    # Verify result
    assert len(result) > 0
    
    # Check benchmark stats
    assert benchmark.stats.mean < 0.05  # 50ms
```

---

## 📊 Manual UAC Examples

### Example 1: Legal Document Upload Flow

**Scenario:** PM manually tests complete upload workflow

**Test Steps:**
```markdown
1. Navigate to http://localhost:3000/upload
   ✅ Page loads correctly

2. Click "Upload File" button
   ✅ File picker opens

3. Select test file: test-data/legal-document.xlsx
   ✅ File name displays

4. Click "Process File"
   ✅ Loading spinner shows
   ✅ Progress bar updates

5. Wait for processing
   ✅ Success message: "File processed successfully"
   ✅ Results display with 5 legal domains extracted

6. Click "View Details" on first result
   ✅ Detail page opens
   ✅ All fields populated correctly

7. Click "Export Results"
   ✅ CSV download starts
   ✅ CSV contains correct data

Result: ✅ PASS - All steps successful
```

---

### Example 2: Error Handling Flow

**Scenario:** Test error scenarios manually

**Test Steps:**
```markdown
1. Upload invalid file (PDF instead of Excel)
   ✅ Error message: "Invalid file type. Please upload Excel file."
   ✅ File picker clears

2. Upload corrupted Excel file
   ✅ Error message: "Unable to process file. Please check file format."

3. Upload empty Excel file
   ✅ Warning: "No data found in file"

4. Test without internet connection
   ✅ Offline message displays
   ✅ Upload button disabled

Result: ✅ PASS - All error scenarios handled correctly
```

---

## 📚 Related

- [testing-protocol.md](../core/testing-protocol.md) - Full testing protocol
- [coding-standards.md](../core/coding-standards.md) - Test structure standards
- [quality-gates.md](../core/quality-gates.md) - Gate #6 (Tests)

---

**Remember:** Every bug fix = regression test, Every new feature = full test coverage!
