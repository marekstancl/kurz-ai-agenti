---
applyTo: "**/*"
---

# ✨ New Feature Workflow

**Version:** 3.0.0  
**Type:** workflow  
**Last Updated:** 2026-01-23  
**Applies To:** Adding new functionality to the system  
**Template:** .github/templates/session-new-feature.md

---

## 🎯 Purpose

**What:** Add new functionality that doesn't exist yet.

**When:** PM requests new feature, capability, or enhancement.

**Key Principle:** Design → Implement → Test → Document. Quality over speed.

---

## 📋 When to Use This Workflow

**✅ Use New Feature when:**
- Adding NEW functionality (something that didn't exist)
- Enhancing existing feature (new capability)
- Building new component/module/service
- Adding new API endpoint
- Creating new UI component
- Implementing new business logic

**❌ Don't use when:**
- Fixing broken functionality → Use `bug-fix.md`
- Improving code without adding features → Use `refactoring.md`
- Syncing UI from design source → Use `ui-sync.md`
- Just exploring options → Use Think-First approach

---

## 🎭 Role & Mindset: Architect → Builder

**Your role for new features:**
````markdown
🎭 Role: Architect (design phase) → Builder (implementation phase)
🎯 Mindset: Design FIRST, code SECOND
📊 Priority: Scalability > Quick win, Quality > Speed
🔍 Approach: Design → Review → Build → Test → Polish
````

**Architect mindset (design phase):**
- ✅ Think about scalability (will this handle 10x load?)
- ✅ Consider edge cases (what could go wrong?)
- ✅ Plan for testing (how will we verify this works?)
- ✅ Design API/interfaces (clear contracts)
- ✅ Think about backwards compatibility

**Builder mindset (implementation phase):**
- ✅ Follow the approved design
- ✅ Write clean, maintainable code
- ✅ Add comprehensive tests
- ✅ Document as you build
- ✅ Think about future maintainers

---

## 🧭 Decision Tree: Feature vs Other Workflows
````
New work requested
│
├─ Is this ADDING something new?
│   ├─ YES → New Feature ✅
│   └─ NO → Continue below
│
├─ Is something BROKEN?
│   ├─ YES → Bug Fix
│   └─ NO → Continue below
│
├─ Improving code without adding features?
│   ├─ YES → Refactoring
│   └─ NO → New Feature
│
├─ Syncing from design source (Figma, AI Studio)?
│   ├─ YES → UI Sync
│   └─ NO → New Feature
│
└─ Just exploring/researching?
    ├─ YES → Think-First approach
    └─ NO → New Feature
````

---

## 🔄 New Feature Process (10 Steps)

**⚠️ CRITICAL: Execute phases sequentially. Design before code!**
````
PHASE 1: DESIGN
   Step 0: Think-First Plan (MANDATORY)
   Step 1: Create Session File + Branch (after approval)
   Step 2: Design Architecture & API
   Step 3: Design Database Schema (if applicable)
   Step 4: Design UI/UX (if applicable)
   ↓
PHASE 2: IMPLEMENTATION
   Step 5: Implement Backend (if applicable)
   Step 6: Implement Frontend (if applicable)
   Step 7: Write Tests (unit + integration)
   ↓
PHASE 3: VERIFICATION
   Step 8: Manual UAC Testing
   Step 9: Documentation & Quality Gates
   Step 10: Final Commit & Handoff
````

---

## 🎨 PHASE 1: DESIGN

### STEP 0: Think-First Plan (MANDATORY)

**🚨 STOP! Design before implementing!**

**According to `think-first.md`:**
````markdown
## 📋 Navrhovaný Plán - New Feature

**Feature:** {Feature name/description}
**Component:** {backend/frontend/full-stack}
**Priority:** {high|medium|low}
**Moje role:** Architect → Builder

### Analýza (Requirements Understanding)

**User Story / Requirement:**
{What does the user need? Why?}

Example: "As a PM, I need to filter translation memories by legal domain, so I can find relevant translations faster."

**Acceptance Criteria:**
- {Criterion 1: User can select legal domain from dropdown}
- {Criterion 2: TM list filters to show only entries from selected domain}
- {Criterion 3: Filter persists across page refreshes}

**Scope:**
- In scope: {What WILL be included}
- Out of scope: {What will NOT be included}
- Future considerations: {What might come later}

### Navrhovaný Přístup (Architecture Design)

**High-Level Design:**

1. **Backend Changes:**
   - New table: legal_domains (if doesn't exist)
   - New API endpoint: GET /api/v1/legal-domains
   - Modified endpoint: GET /api/v1/tm-entries (add domain filter param)
   - New service: LegalDomainService

2. **Frontend Changes:**
   - New component: LegalDomainDropdown
   - Modified component: TMList (add filter)
   - New hook: useLegalDomains
   - State management: Persist filter in localStorage

3. **Database Changes:**
   - Migration: Add legal_domain_id to translation_memories table
   - Seed data: Pre-populate legal_domains table

**Implementation Steps:**

**Phase 1: Design** ({time estimate})
1. Design API contracts
2. Design DB schema
3. Design UI mockup (if needed)
4. Review with PM → Get approval

**Phase 2: Backend** ({time estimate})
5. Create database migration
6. Create LegalDomain model
7. Create legal_domains API endpoint
8. Add domain filter to tm-entries endpoint
9. Write backend tests

**Phase 3: Frontend** ({time estimate})
10. Create LegalDomainDropdown component
11. Create useLegalDomains hook
12. Integrate filter into TMList
13. Add localStorage persistence
14. Write frontend tests

**Phase 4: Verification** ({time estimate})
15. Integration testing
16. Manual UAC testing
17. Documentation updates

### Soubory

**Will create:**
- Backend:
  - `backend/migrations/YYYYMMDD_add_legal_domains.sql` - NEW
  - `backend/app/models/legal_domain.py` - NEW
  - `backend/app/api/v1/legal_domains.py` - NEW
  - `backend/app/services/legal_domain_service.py` - NEW
  - `backend/tests/unit/test_legal_domain.py` - NEW
  - `backend/tests/integration/test_legal_domains_api.py` - NEW

- Frontend:
  - `frontend/src/components/LegalDomains/LegalDomainDropdown.tsx` - NEW
  - `frontend/src/hooks/useLegalDomains.ts` - NEW
  - `frontend/src/services/legalDomainService.ts` - NEW
  - `frontend/tests/components/LegalDomainDropdown.test.tsx` - NEW

**Will modify:**
- Backend:
  - `backend/app/api/v1/tm_entries.py` - add filter param
  - `backend/app/models/translation_memory.py` - add legal_domain_id FK

- Frontend:
  - `frontend/src/pages/TMAlignment.tsx` - integrate dropdown
  - `frontend/src/components/TMList.tsx` - use filter

### Dokumentace

**Will update:**
- `docs/architecture/database-erd.md` - add legal_domains table
- `docs/developers/backend/api-design.md` - document new endpoints
- `docs/developers/frontend/components.md` - document new components
- `docs/stakeholders/ui-guide.md` - show new filter feature
- `CHANGELOG.md` - add feature entry

### Rizika & Edge Cases

**Technical Risks:**
- Migration might fail if data inconsistent → Test on dev DB first
- Filter performance with 10k+ TM entries → Add DB index

**Edge Cases:**
- User has no legal domains → Show "No domains available" message
- TM entry has NULL legal_domain_id → Show in "Uncategorized"
- Dropdown loading fails → Show error, allow retry

**Mitigation:**
- Thorough testing with edge case data
- Error handling at every layer
- Rollback plan if migration fails

### Testing Strategy

**Unit Tests:**
- Backend: LegalDomain model, service layer
- Frontend: LegalDomainDropdown component, useLegalDomains hook

**Integration Tests:**
- API endpoints with real DB
- Frontend-backend integration

**Manual UAC:**
- Happy path: Select domain, see filtered results
- Edge cases: No domains, network error, persistence

**Coverage Target:** >90% for new code

### Estimated Duration

- Phase 1 (Design): {2 hours}
- Phase 2 (Backend): {4 hours}
- Phase 3 (Frontend): {3 hours}
- Phase 4 (Verification): {2 hours}

**Total:** {11 hours} over {2-3 sessions}

**Můžu pokračovat s tímto plánem?**
````

**Wait for PM approval (GO/REVISE) before Step 1!**

---

### STEP 1: Create Session File + Branch (After Approval)

**After PM approves plan:**

#### 1.1: Create Session File
````bash
# Copy template
cp .ai-workflow/templates/session-new-feature.md \
   .ai-workflow/workplace/sessions/active/$(date +%Y-%m-%d)-{feature-topic}.md

# Or create with frontmatter:
````
````yaml
---
session_id: new-feature-YYYY-MM-DD-{topic}
type: new-feature
status: active
priority: {high|medium|low}
started: YYYY-MM-DD HH:MM CET
estimated_duration: {X hours}
complexity: {low|medium|high}
---
````

**Fill session file with:**
- Approved design/plan
- Task breakdown (from plan)
- Acceptance criteria

#### 1.2: Create Git Branch
````bash
# Create feature branch
git checkout -b session/$(date +%Y-%m-%d)-{feature-topic}

# Example:
git checkout -b session/2026-01-23-legal-domains-filter
````

#### 1.3: Confirm to PM
````markdown
✅ Session initialized for new feature

**Session file:** sessions/active/{filename}.md
**Branch:** session/{date}-{feature-topic}
**Estimated duration:** {X hours}
**Complexity:** {low|medium|high}

**Phases:**
1. Design (Steps 2-4)
2. Implementation (Steps 5-7)
3. Verification (Steps 8-10)

Ready to start design phase (Step 2).
````

---

### STEP 2: Design Architecture & API

**Purpose:** Design technical architecture before writing code.

**See:** `project-guide.md` for project-specific architecture patterns

#### 2.1: API Design (If Backend Feature)
````markdown
## 🏗️ API Design

### New Endpoints

#### GET /api/v1/legal-domains

**Purpose:** Retrieve list of legal domains

**Request:**
```http
GET /api/v1/legal-domains HTTP/1.1
Authorization: Bearer {token}
```

**Response:**
```json
{
  "data": [
    {
      "id": 1,
      "name": "Contract Law",
      "code": "CONTRACT",
      "description": "Contracts and agreements",
      "created_at": "2026-01-20T10:00:00Z"
    },
    {
      "id": 2,
      "name": "Corporate Law",
      "code": "CORPORATE",
      "description": "Corporate governance",
      "created_at": "2026-01-20T10:00:00Z"
    }
  ],
  "total": 2
}
```

**Status Codes:**
- 200: Success
- 401: Unauthorized
- 500: Server Error

**Business Rules:**
- Returns only domains user has access to
- Sorted alphabetically by name

---

#### GET /api/v1/tm-entries (Modified)

**Changes:** Add `legal_domain_id` query parameter

**Request:**
```http
GET /api/v1/tm-entries?legal_domain_id=1&page=1&size=20 HTTP/1.1
Authorization: Bearer {token}
```

**Response:**
```json
{
  "data": [
    {
      "id": 123,
      "source": "Hello",
      "target": "Hola",
      "legal_domain_id": 1,
      "legal_domain_name": "Contract Law",
      ...
    }
  ],
  "total": 156,
  "page": 1,
  "size": 20
}
```

**Business Rules:**
- If legal_domain_id not provided → return all
- If legal_domain_id = 0 → return only uncategorized
- Invalid domain_id → 400 Bad Request
````

#### 2.2: Data Models
````markdown
## 📊 Data Models

### LegalDomain

**SQLAlchemy Model:**
```python
class LegalDomain(Base):
    """Legal domain for categorizing translation memories."""
    
    __tablename__ = "legal_domains"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    code = Column(String(20), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relationships
    translation_memories = relationship("TranslationMemory", back_populates="legal_domain")
```

**Pydantic Schemas:**
```python
class LegalDomainBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    code: str = Field(..., min_length=1, max_length=20)
    description: Optional[str] = None
    active: bool = True

class LegalDomainCreate(LegalDomainBase):
    pass

class LegalDomainResponse(LegalDomainBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
```

### TranslationMemory (Modified)

**Changes:** Add legal_domain_id foreign key
```python
class TranslationMemory(Base):
    # ... existing fields ...
    
    legal_domain_id = Column(Integer, ForeignKey("legal_domains.id"), nullable=True, index=True)
    
    # Relationships
    legal_domain = relationship("LegalDomain", back_populates="translation_memories")
```
````

#### 2.3: Service Layer Design
````markdown
## 🔧 Service Layer

### LegalDomainService

**Responsibilities:**
- CRUD operations for legal domains
- Business logic validation
- Access control (user permissions)

**Key Methods:**
```python
class LegalDomainService:
    def get_all(self, db: Session, user_id: int) -> List[LegalDomain]:
        """Get all legal domains user has access to."""
        
    def get_by_id(self, db: Session, domain_id: int) -> Optional[LegalDomain]:
        """Get legal domain by ID."""
        
    def create(self, db: Session, domain: LegalDomainCreate, user_id: int) -> LegalDomain:
        """Create new legal domain."""
        
    def update(self, db: Session, domain_id: int, updates: LegalDomainUpdate) -> LegalDomain:
        """Update existing legal domain."""
        
    def delete(self, db: Session, domain_id: int) -> bool:
        """Soft delete legal domain."""
```

### TMService (Modified)

**Changes:** Add filtering by legal_domain_id
```python
def get_tm_entries(
    db: Session,
    user_id: int,
    legal_domain_id: Optional[int] = None,
    page: int = 1,
    size: int = 20
) -> Tuple[List[TranslationMemory], int]:
    """Get TM entries with optional legal domain filter."""
    query = db.query(TranslationMemory).filter(...)
    
    if legal_domain_id is not None:
        if legal_domain_id == 0:
            # Uncategorized
            query = query.filter(TranslationMemory.legal_domain_id.is_(None))
        else:
            # Specific domain
            query = query.filter(TranslationMemory.legal_domain_id == legal_domain_id)
    
    # ... pagination logic ...
```
````

---

### STEP 3: Design Database Schema (If Applicable)

**Purpose:** Plan database changes before implementing.

#### 3.1: ERD Update
````markdown
## 📐 Database Schema Design

### New Table: legal_domains
```sql
CREATE TABLE legal_domains (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    code VARCHAR(20) NOT NULL UNIQUE,
    description TEXT,
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE,
    
    -- Indexes
    CONSTRAINT legal_domains_name_key UNIQUE (name),
    CONSTRAINT legal_domains_code_key UNIQUE (code)
);

CREATE INDEX idx_legal_domains_name ON legal_domains(name);
CREATE INDEX idx_legal_domains_code ON legal_domains(code);
CREATE INDEX idx_legal_domains_active ON legal_domains(active);
```

### Modified Table: translation_memories
```sql
-- Add foreign key column
ALTER TABLE translation_memories 
ADD COLUMN legal_domain_id INTEGER REFERENCES legal_domains(id) ON DELETE SET NULL;

-- Add index for filtering
CREATE INDEX idx_translation_memories_legal_domain 
ON translation_memories(legal_domain_id);
```

### Seed Data
```sql
-- Pre-populate common legal domains
INSERT INTO legal_domains (name, code, description) VALUES
('Contract Law', 'CONTRACT', 'Contracts and commercial agreements'),
('Corporate Law', 'CORPORATE', 'Corporate governance and compliance'),
('Intellectual Property', 'IP', 'Patents, trademarks, copyrights'),
('Labor Law', 'LABOR', 'Employment and labor relations'),
('Tax Law', 'TAX', 'Taxation and fiscal matters');
```

### Migration Strategy

1. Create legal_domains table
2. Add legal_domain_id column to translation_memories (nullable)
3. Run seed data
4. LATER: Backfill existing TM entries (separate task)
5. NEVER: Make legal_domain_id NOT NULL (many TMs uncategorized)
````

#### 3.2: Migration File
````markdown
## 📝 Migration Plan

**File:** `backend/migrations/20260123_add_legal_domains.sql`

**Rollback Plan:** 
```sql
-- If migration fails
ALTER TABLE translation_memories DROP COLUMN legal_domain_id;
DROP TABLE legal_domains CASCADE;
```

**Testing:**
- Test on dev database first
- Verify foreign key constraints work
- Verify indexes created
- Verify seed data inserted
````

---

### STEP 4: Design UI/UX (If Applicable)

**Purpose:** Plan user interface before building.

#### 4.1: Component Design
````markdown
## 🎨 UI/UX Design

### Component: LegalDomainDropdown

**Location:** `frontend/src/components/LegalDomains/LegalDomainDropdown.tsx`

**Props:**
```typescript
interface LegalDomainDropdownProps {
  value: number | null;  // Selected domain ID
  onChange: (domainId: number | null) => void;
  placeholder?: string;
  disabled?: boolean;
  showAll?: boolean;  // Show "All" option
  showUncategorized?: boolean;  // Show "Uncategorized" option
}
```

**Visual Design:**
````
┌─────────────────────────────────────┐
│  Legal Domain: [▼ Select domain  ] │  ← Dropdown
└─────────────────────────────────────┘

When opened:
┌─────────────────────────────────────┐
│  Legal Domain: [▼ Contract Law    ] │
├─────────────────────────────────────┤
│  All domains                         │ ← Option (if showAll)
│  Uncategorized                       │ ← Option (if showUncategorized)
│  ────────────────────────────────────│
│  Contract Law                        │
│  Corporate Law                       │
│  Intellectual Property               │
│  Labor Law                           │
│  Tax Law                             │
└─────────────────────────────────────┘
````

**States:**
- Loading: Show skeleton/spinner
- Empty: "No domains available"
- Error: "Failed to load domains" + retry button
- Success: Show dropdown with domains

**Styling:**
- Tailwind CSS (project standard)
- Consistent with existing dropdowns
- Mobile responsive

### Integration: TMAlignment Page

**Changes to `frontend/src/pages/TMAlignment.tsx`:**
````
┌──────────────────────────────────────────┐
│  TM Alignment                            │
├──────────────────────────────────────────┤
│  Legal Domain: [▼ All domains        ]  │  ← NEW
│  Search: [____________]  [Search]       │
├──────────────────────────────────────────┤
│  TM Entries (filtered):                  │
│  ┌────────────────────────────────────┐ │
│  │ Source: Hello                       │ │
│  │ Target: Hola                        │ │
│  │ Domain: Contract Law                │ │  ← Show domain
│  └────────────────────────────────────┘ │
│  ┌────────────────────────────────────┐ │
│  │ Source: Agreement                   │ │
│  │ Target: Acuerdo                     │ │
│  │ Domain: Contract Law                │ │
│  └────────────────────────────────────┘ │
└──────────────────────────────────────────┘
````

### State Management

**Filter state stored in:**
- Component state (React useState)
- localStorage (key: "tm_legal_domain_filter")
- Persists across page refreshes

**URL params (optional future enhancement):**
- `?domain=1` in URL
- Shareable filtered view
````

#### 4.2: User Flows
````markdown
## 🔄 User Flows

### Happy Path: Filter TM by Domain

1. User navigates to TM Alignment page
2. User sees "Legal Domain" dropdown (default: "All")
3. User clicks dropdown → sees list of domains
4. User selects "Contract Law"
5. TM list refreshes → shows only Contract Law entries
6. User refreshes page → filter persists (localStorage)

### Edge Case: No Domains

1. User navigates to TM Alignment page
2. Dropdown shows "Loading..."
3. API returns empty list
4. Dropdown shows "No domains available"
5. TM list shows all entries (no filter)

### Edge Case: Network Error

1. User selects domain
2. API call fails
3. Error message: "Failed to filter. Try again."
4. Retry button appears
5. User clicks retry → API call repeats

### Edge Case: Uncategorized Entries

1. User selects "Uncategorized" from dropdown
2. TM list shows entries with legal_domain_id = NULL
3. These are TMs not yet categorized
````

---

## 🛠️ PHASE 2: IMPLEMENTATION

### STEP 5: Implement Backend (If Applicable)

**Purpose:** Build backend according to design.

**See:** `coding-standards.md` for Python/FastAPI standards

#### 5.1: Database Migration
````bash
# Create migration file
touch backend/migrations/20260123_add_legal_domains.sql
````
````sql
-- backend/migrations/20260123_add_legal_domains.sql

-- Create legal_domains table
CREATE TABLE legal_domains (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    code VARCHAR(20) NOT NULL UNIQUE,
    description TEXT,
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE
);

-- Create indexes
CREATE INDEX idx_legal_domains_name ON legal_domains(name);
CREATE INDEX idx_legal_domains_code ON legal_domains(code);
CREATE INDEX idx_legal_domains_active ON legal_domains(active);

-- Add legal_domain_id to translation_memories
ALTER TABLE translation_memories 
ADD COLUMN legal_domain_id INTEGER REFERENCES legal_domains(id) ON DELETE SET NULL;

CREATE INDEX idx_translation_memories_legal_domain 
ON translation_memories(legal_domain_id);

-- Seed data
INSERT INTO legal_domains (name, code, description) VALUES
('Contract Law', 'CONTRACT', 'Contracts and commercial agreements'),
('Corporate Law', 'CORPORATE', 'Corporate governance and compliance'),
('Intellectual Property', 'IP', 'Patents, trademarks, copyrights'),
('Labor Law', 'LABOR', 'Employment and labor relations'),
('Tax Law', 'TAX', 'Taxation and fiscal matters');
````

**Run migration:**
````bash
# See project-guide.md for migration command
{migration command from project-guide.md}

# Example:
docker-compose exec backend alembic upgrade head
````

**Verify migration:**
````bash
# Check tables created
docker-compose exec db psql -U postgres -d translation_db -c "\dt"

# Check data seeded
docker-compose exec db psql -U postgres -d translation_db -c "SELECT * FROM legal_domains;"
````

**Document in session file:**
````markdown
## ✅ Migration Applied

**File:** `backend/migrations/20260123_add_legal_domains.sql`
**Status:** ✅ Success
**Tables created:** legal_domains
**Columns added:** translation_memories.legal_domain_id
**Seed data:** 5 legal domains inserted
````

#### 5.2: Models
````python
# backend/app/models/legal_domain.py

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class LegalDomain(Base):
    """Legal domain model for TM categorization."""
    
    __tablename__ = "legal_domains"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    code = Column(String(20), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    active = Column(Boolean, default=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    translation_memories = relationship(
        "TranslationMemory",
        back_populates="legal_domain",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<LegalDomain(id={self.id}, name={self.name}, code={self.code})>"
````
````python
# backend/app/schemas/legal_domain.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class LegalDomainBase(BaseModel):
    """Base schema for Legal Domain."""
    name: str = Field(..., min_length=1, max_length=100, description="Domain name")
    code: str = Field(..., min_length=1, max_length=20, description="Domain code")
    description: Optional[str] = Field(None, description="Domain description")
    active: bool = Field(True, description="Whether domain is active")

class LegalDomainCreate(LegalDomainBase):
    """Schema for creating Legal Domain."""
    pass

class LegalDomainUpdate(BaseModel):
    """Schema for updating Legal Domain."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    code: Optional[str] = Field(None, min_length=1, max_length=20)
    description: Optional[str] = None
    active: Optional[bool] = None

class LegalDomainResponse(LegalDomainBase):
    """Schema for Legal Domain response."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
````

#### 5.3: API Endpoints
````python
# backend/app/api/v1/legal_domains.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.legal_domain import LegalDomain
from app.schemas.legal_domain import LegalDomainCreate, LegalDomainResponse, LegalDomainUpdate
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[LegalDomainResponse])
async def get_legal_domains(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get all active legal domains."""
    domains = db.query(LegalDomain).filter(LegalDomain.active == True).order_by(LegalDomain.name).all()
    return domains

@router.get("/{domain_id}", response_model=LegalDomainResponse)
async def get_legal_domain(
    domain_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get legal domain by ID."""
    domain = db.query(LegalDomain).filter(LegalDomain.id == domain_id).first()
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Legal domain with id {domain_id} not found"
        )
    return domain

@router.post("/", response_model=LegalDomainResponse, status_code=status.HTTP_201_CREATED)
async def create_legal_domain(
    domain: LegalDomainCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Create new legal domain."""
    # Check for duplicates
    existing = db.query(LegalDomain).filter(
        (LegalDomain.name == domain.name) | (LegalDomain.code == domain.code)
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Legal domain with this name or code already exists"
        )
    
    db_domain = LegalDomain(**domain.dict())
    db.add(db_domain)
    db.commit()
    db.refresh(db_domain)
    
    return db_domain
````

**Modify existing endpoint:**
````python
# backend/app/api/v1/tm_entries.py (MODIFIED)

@router.get("/", response_model=TMEntriesResponse)
async def get_tm_entries(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    legal_domain_id: Optional[int] = Query(None, description="Filter by legal domain"),  # ← NEW
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get TM entries with optional legal domain filter."""
    query = db.query(TranslationMemory).filter