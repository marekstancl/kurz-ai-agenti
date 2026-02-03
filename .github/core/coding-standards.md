---
applyTo: "**/*"
---

# 💻 Coding Standards

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Overview

**Purpose:** Tech stack standardy pro konzistentní, maintainable kód

**Philosophy:** Standardy = předvídatelnost, čitelnost, safety

**Scope:** Python (FastAPI), TypeScript (React), SQL, Git

---

## 🚨 GOLDEN RULES (Quick Reference)

### Rule #0.1: Think-First
Navrhni plán → čekej na schválení → implementuj  
See: [think-first.md](think-first.md)

### Rule #0.2: Quality Gates
Pre-commit checklist PŘED KAŽDÝM commitem  
See: [quality-gates.md](quality-gates.md)

### Rule #0.3: Atomic Commits
```
type(scope): description (YYYY-MM-DD HH:MM CET)
```
See: [git-commit-protocol.md](git-commit-protocol.md)

### Rule #0.4: Branch Discipline
```
VŽDY: session/YYYY-MM-DD-{topic}
NIKDY: main bez schválení PM
```

### Rule #0.5: Documentation Standards
All docs in Docusaurus format with MDX escaping  
See: [documentation-protocol.md](documentation-protocol.md)

---

## 🐍 Python (FastAPI)

### File Structure
```
backend/
├── app/
│   ├── main.py
│   ├── core/ (config, security, database)
│   ├── models/ (SQLAlchemy)
│   ├── schemas/ (Pydantic)
│   ├── api/v1/ (endpoints)
│   ├── services/ (business logic)
│   └── utils/
└── tests/ (unit, integration)
```

### Type Hints (MANDATORY)
```python
def get_domain(db: Session, domain_id: int) -> Optional[LegalDomain]:
    """Get legal domain by ID."""
    return db.query(LegalDomain).filter_by(id=domain_id).first()
```

### Pydantic Schemas (MANDATORY for API)
```python
from pydantic import BaseModel, Field

class LegalDomainCreate(BaseModel):
    name: str = Field(..., min_length=1)
    code: str = Field(..., min_length=2)
    description: Optional[str] = None
```

### Async/Await (Use for I/O)
```python
@router.get("/domains/{id}")
async def get_domain(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(LegalDomain).where(LegalDomain.id == id))
    return result.scalar_one_or_none()
```

### Error Handling
```python
try:
    domain = await get_domain(domain_id)
    if not domain:
        raise HTTPException(status_code=404, detail="Not found")
    return domain
except SQLAlchemyError as e:
    logger.error(f"DB error: {e}")
    raise HTTPException(status_code=500, detail="Database error")
```

### Logging (No print!)
```python
import logging
logger = logging.getLogger(__name__)

logger.info(f"Creating domain: {domain.name}")
logger.error(f"Error: {e}", exc_info=True)
```

**Examples:** [examples/coding-examples.md](../examples/coding-examples.md#python-type-hints)

---

## ⚛️ TypeScript/React

### File Structure
```
frontend/src/
├── components/ (common, feature-specific)
├── pages/
├── services/ (API calls)
├── hooks/ (custom hooks)
├── types/ (interfaces)
└── utils/
```

### Interfaces (MANDATORY)
```typescript
interface LegalDomain {
  id: number;
  name: string;
  code: string;
  description: string | null;
}

interface LegalDomainFormProps {
  initialData?: LegalDomain;
  onSubmit: (data: LegalDomainCreate) => Promise<void>;
}
```

### Functional Components + Hooks
```typescript
export const LegalDomainList: React.FC<LegalDomainListProps> = ({
  customerId,
  onSelect
}) => {
  const [domains, setDomains] = useState<LegalDomain[]>([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchDomains();
  }, [customerId]);
  
  return <div>{/* ... */}</div>;
};
```

### Custom Hooks (Reusable Logic)
```typescript
export const useLegalDomains = (customerId?: number) => {
  const [domains, setDomains] = useState<LegalDomain[]>([]);
  const [loading, setLoading] = useState(true);
  
  const fetchDomains = useCallback(async () => {
    const data = await getLegalDomains(customerId);
    setDomains(data);
  }, [customerId]);
  
  return { domains, loading, refetch: fetchDomains };
};
```

### Tailwind CSS (Utility-First)
```typescript
<div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg">
  <h3 className="text-xl font-semibold text-gray-900">{domain.name}</h3>
</div>
```

### API Service Layer (MANDATORY)
```typescript
// services/legalDomainService.ts
export const getLegalDomains = async (): Promise<LegalDomain[]> => {
  const response = await api.get<LegalDomain[]>('/api/v1/legal-domains');
  return response.data;
};

// Component uses service, NOT direct fetch!
const { domains } = useLegalDomains();
```

**Examples:** [examples/coding-examples.md](../examples/coding-examples.md#typescript-interfaces)

---

## 🗄️ SQL/Database

### Use ORM (Avoid Raw SQL)
```python
# ✅ CORRECT
domains = db.query(LegalDomain).filter(LegalDomain.name.like('%contract%')).all()

# ❌ WRONG - SQL injection risk!
query = f"SELECT * FROM legal_domains WHERE name = '{name}'"
```

### Database Migrations
```sql
-- Descriptive filename, proper constraints
-- Example: 001_create_users_table.sql

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

**Note:** Migration tool depends on project (Alembic, raw SQL, Flyway, etc.). Check [project-guide.md](project-guide.md) for your project's approach.

**Examples:** [examples/coding-examples.md](../examples/coding-examples.md#sql)

---

## 📝 Documentation in Code

### Comments (Explain WHY, not WHAT)
```python
# ✅ CORRECT
# Normalize by max length (not min) to penalize different-length matches
distance = levenshtein_distance(source, target)

# ❌ WRONG
# Calculate distance
distance = levenshtein_distance(source, target)
```

### TODO Comments
```python
# During development: OK
# TODO: Add pagination (Session 2)

# Before commit: MOVE to bugs.md or session file!
# Production code should NOT have TODO comments!
```

---

## 🧪 Testing

**See:** [testing-protocol.md](testing-protocol.md)

### Test Structure
```
tests/
├── unit/
│   └── test_legal_domain_service.py
└── integration/
    └── test_legal_domain_api.py
```

### Descriptive Names
```python
def test_get_legal_domain_returns_domain_when_exists():
    """Test that get_legal_domain returns domain when ID exists."""
    pass

def test_create_legal_domain_raises_error_when_duplicate_name():
    """Test duplicate name raises HTTPException."""
    pass
```

---

## ⚠️ Anti-Patterns (Avoid)

### God Objects
```python
# ❌ WRONG - too many responsibilities
class DocumentProcessor:
    def parse(self): pass
    def translate(self): pass
    def export(self): pass
    def send_email(self): pass
    # ... 20 more methods

# ✅ CORRECT - separation of concerns
class DocumentParser: pass
class Translator: pass
class Exporter: pass
```

### Prop Drilling
```typescript
// ❌ WRONG - drilling 4 levels
<App userId={userId}>
  <Page userId={userId}>
    <Component userId={userId}>
      <SubComponent userId={userId} />
    </Component>
  </Page>
</App>

// ✅ CORRECT - use context
<UserContext.Provider value={user}>
  <App><Page><Component><SubComponent /></Component></Page></App>
</UserContext.Provider>
```

---

## ✅ Pre-Commit Code Quality

```markdown
□ Type hints present (Python)
□ Interfaces defined (TypeScript)
□ No console.log/print() in prod
□ No TODO comments in prod
□ Imports ordered
□ No unused imports
□ Docstrings for public functions
□ Error handling present
□ No hardcoded credentials
□ Tests written (if applicable)
```

Full checklist: [quality-gates.md](quality-gates.md)

---

## 📚 Related

- [quality-gates.md](quality-gates.md) - Pre-commit workflow
- [git-commit-protocol.md](git-commit-protocol.md) - Commit standards
- [testing-protocol.md](testing-protocol.md) - Testing guidelines
- [examples/coding-examples.md](../examples/coding-examples.md) - Code examples

---

**Remember:** Standards make code predictable. When in doubt, ask PM!
