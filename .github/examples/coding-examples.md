# Coding Standards Examples

## Python Type Hints

**✅ CORRECT:**
```python
def get_legal_domain(db: Session, domain_id: int) -> Optional[LegalDomain]:
    """Get legal domain by ID."""
    return db.query(LegalDomain).filter(LegalDomain.id == domain_id).first()
```

**❌ WRONG:**
```python
def get_legal_domain(db, domain_id):
    return db.query(LegalDomain).filter(LegalDomain.id == domain_id).first()
```

## TypeScript Interfaces

**✅ CORRECT:**
```typescript
interface LegalDomain {
  id: number;
  name: string;
  code: string;
  description: string | null;
}

export const LegalDomainCard: React.FC<{ domain: LegalDomain }> = ({ domain }) => {
  return <div>{domain.name}</div>;
};
```

**❌ WRONG:**
```typescript
export const LegalDomainCard = ({ domain }) => {  // No types!
  return <div>{domain.name}</div>;
};
```

## Error Handling

**✅ CORRECT:**
```python
try:
    domain = await get_domain(domain_id)
    if not domain:
        raise HTTPException(status_code=404, detail=f"Domain {domain_id} not found")
    return domain
except SQLAlchemyError as e:
    logger.error(f"Database error: {e}")
    raise HTTPException(status_code=500, detail="Database error")
```

**❌ WRONG:**
```python
domain = await get_domain(domain_id)
if not domain:
    raise Exception("Not found")  # Generic exception!
return domain
```

## SQL - Use ORM

**✅ CORRECT:**
```python
domains = db.query(LegalDomain).filter(LegalDomain.name.like('%contract%')).all()
```

**❌ WRONG:**
```python
domain_name = request.query_params.get('name')
query = f"SELECT * FROM legal_domains WHERE name = '{domain_name}'"  # SQL INJECTION!
```

Více viz [core/coding-standards.md](../core/coding-standards.md)
