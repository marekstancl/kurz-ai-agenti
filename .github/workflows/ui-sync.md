---
applyTo: "**/*"
---

# 🎨 UI Sync Workflow

**Version:** 3.0.0  
**Last Updated:** 2026-01-24

---

## 🎯 Purpose

**Problem:** Design exists externally (Google AI Studio, Figma, etc.) and needs 1:1 integration.

**Solution:** Systematic INJECTION workflow - use what's provided, don't invent.

**✅ Use when:** Design exists, PM says "implement 1:1", visual fidelity critical

**❌ Don't use:** Designing from scratch (→ new-feature.md), incomplete design

---

## 🚨 Critical Rules

**Rule #1: 1:1 Visual Fidelity**
- Final result MUST match design exactly
- Same colors, spacing, typography, layout, interactions
- ❌ "Close enough" NOT acceptable
- ❌ NO "improvements" without PM approval

**Rule #2: Injection Algorithm**
```
Extract ALL properties → Map to tech stack → Inject WITHOUT modification → Verify 1:1
```

**Rule #3: Ask Before Assuming**
- Design unclear/incomplete? → Ask PM
- ❌ DON'T guess or use "standard" patterns

---

## 📊 Workflow (5 Phases)

```
PHASE 1: Discovery & Gap Analysis
   ↓
PHASE 2: Extraction & Mapping
   ↓
PHASE 3: Implementation (Injection)
   ↓
PHASE 4: Verification & Validation
   ↓
PHASE 5: Polish & Optimization
```

---

## PHASE 1: Discovery & Gap Analysis

**Step 1.1: Receive Design Source**

PM provides: Code snippet / Figma link / Screenshot / Live URL

Verify:
- Design accessible ✅
- Design complete (not draft) ✅
- Design approved ✅
- Target component identified ✅

**Step 1.2: Analyze Completeness**

Check for:
- **Visual:** Colors, typography, spacing, sizing, borders, shadows, layout
- **Interactive:** Hover, active, focus, disabled, loading, error states
- **Responsive:** Mobile/tablet/desktop breakpoints

**If missing:** Ask PM for clarification (DON'T guess!)

**Step 1.3: Identify Target Component**

```bash
# Locate injection point
ls frontend/src/components/

# Target file
frontend/src/components/[Component]/[Component].tsx
```

**Step 1.4: Gap Analysis Report**

```markdown
## 🔍 UI Sync Discovery Report

**Design Source:** [Google AI Studio / Figma / Screenshot]
**Target Component:** `frontend/src/components/[Component].tsx`

### ✅ Complete:
- Colors, typography, spacing, layout

### ❓ Missing/Unclear:
- Responsive behavior: Mobile breakpoint not specified
- Error states: Error message styling not shown

### 🎯 Approach:
Injection Algorithm - Extract → Map to Tailwind → Inject

### ⚠️ Decisions Needed:
1. Mobile breakpoint?
2. Error state styling?

Waiting for PM input...
```

---

## PHASE 2: Extraction & Mapping

**Step 2.1: Extract Visual Properties**

```markdown
### Colors
- Primary: #3B82F6 (blue-500)
- Text: #0F172A (slate-900)
- Border: #E2E8F0 (slate-200)
- Hover: #2563EB (blue-600)

### Typography
- Heading: 20px, font-semibold (text-xl font-semibold)
- Body: 14px (text-sm)

### Spacing
- Card padding: 24px (p-6)
- Gap: 16px (gap-4)

### Layout
- Container: flex flex-col
- Card: rounded-lg shadow-md

### Interactions
- Hover: scale(1.02) + shadow-lg
- Transition: 200ms ease
```

**Step 2.2: Map to Tech Stack**

Project uses: React + TypeScript + Tailwind

```typescript
// Mapping
Primary Button: "bg-blue-500 hover:bg-blue-600 text-white"
Card: "p-6 rounded-lg shadow-md border border-slate-200"
Hover: "hover:scale-102 hover:shadow-lg transition-all duration-200"
```

**Step 2.3: Component Structure Plan**

```typescript
// Component hierarchy
Component (root)
├─ Card Container (flex flex-col)
│  ├─ Header (flex justify-between)
│  │  ├─ Title (text-xl font-semibold)
│  │  └─ Badge (text-xs rounded)
│  ├─ Body (grid gap-4)
│  │  ├─ Field 1
│  │  ├─ Field 2
│  │  └─ Field 3
│  └─ Footer (flex gap-2)
│     ├─ Button 1
│     └─ Button 2
```

---

## PHASE 3: Implementation (Injection)

**Step 3.1: Create Component**

```bash
mkdir -p frontend/src/components/[Component]
touch frontend/src/components/[Component]/[Component].tsx
```

**Step 3.2: Inject Code (1:1 from extraction)**

```typescript
// frontend/src/components/[Component]/[Component].tsx

import React from 'react';

interface ComponentProps {
  // props from design
}

export const Component: React.FC<ComponentProps> = (props) => {
  return (
    <div className="flex flex-col w-full max-w-md rounded-lg shadow-md border border-slate-200 bg-white p-6 hover:scale-102 hover:shadow-lg transition-all duration-200">
      {/* Header */}
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-xl font-semibold text-slate-900">
          {props.title}
        </h3>
      </div>
      
      {/* Body - inject exactly as designed */}
      <div className="grid gap-4">
        {/* Content from design */}
      </div>
      
      {/* Footer */}
      <div className="flex gap-2 mt-4">
        {/* Buttons from design */}
      </div>
    </div>
  );
};
```

**Step 3.3: Document Injection**

```markdown
## 🎨 UI Sync Implementation

**Design Source:** Google AI Studio
**Target:** `[Component].tsx`
**Method:** Tailwind CSS (1:1 mapping)

### Injected:
- Colors: blue-500, slate-900, slate-200
- Typography: text-xl, text-sm
- Spacing: p-6, gap-4
- Layout: flex flex-col, rounded-lg
- Interactions: hover:scale-102, transition-all

### Verification: ⏳ Pending
```

---

## PHASE 4: Verification & Validation

**Step 4.1: Visual Comparison**

```markdown
1. Run dev server: npm run dev
2. Navigate to component
3. Open design source side-by-side
4. Compare pixel-by-pixel:
   □ Colors match exactly
   □ Spacing matches exactly
   □ Typography matches exactly
   □ Layout matches exactly
5. Take screenshot if confirmed
```

**Step 4.2: Interaction Testing**

```markdown
**States:**
□ Default: Correct
□ Hover: Smooth, correct colors
□ Focus: Ring visible, keyboard works
□ Active: Buttons respond
□ Loading: Spinner shows (if applicable)
□ Error: Messages display (if applicable)
```

**Step 4.3: Responsive Testing**

```markdown
**Breakpoints:**
□ Mobile (375px): Layout adapts, no scroll
□ Tablet (768px): Uses space appropriately
□ Desktop (1024px+): Max-width respected
```

**Step 4.4: Verification Report**

```markdown
## ✅ UI Sync Verification Report

**Component:** [Component]
**Date:** YYYY-MM-DD

### Visual Fidelity: ✅ PASS
- [x] Colors match
- [x] Typography matches
- [x] Spacing matches
- [x] Layout matches
- [x] Interactions work

**Deviations:** None

### Final Assessment: ✅ READY FOR PRODUCTION

Component matches design with 1:1 fidelity.
```

**Wait for PM approval before Phase 5**

---

## PHASE 5: Polish & Optimization

**Only AFTER PM approves 1:1 match!**

**Step 5.1: Code Optimization**

```typescript
// BEFORE
<div className="text-sm text-slate-700">...</div>
<div className="text-sm text-slate-700">...</div>

// AFTER (extract repeated classes)
const textStyles = "text-sm text-slate-700";
<div className={textStyles}>...</div>
<div className={textStyles}>...</div>
```

**Rules:**
- ✅ Extract repeated class strings
- ✅ Add TypeScript strict types
- ✅ Improve performance (memoization)
- ❌ NO visual changes without PM approval

**Step 5.2: Documentation**

```markdown
# Component

## Overview
Description

## Source
Design synced from: [Source] (YYYY-MM-DD)
Visual fidelity: 1:1 verified

## Usage
\`\`\`typescript
import { Component } from '@/components/Component';

<Component prop={value} />
\`\`\`

## Props
| Prop | Type | Required | Description |
|------|------|----------|-------------|
| ... | ... | ... | ... |
```

**Step 5.3: Testing**

```typescript
// Component tests
import { render, screen, fireEvent } from '@testing-library/react';

describe('Component', () => {
  it('renders correctly', () => {
    render(<Component {...props} />);
    expect(screen.getByText('...')).toBeInTheDocument();
  });
  
  it('handles interactions', () => {
    const onClick = jest.fn();
    render(<Component onClick={onClick} />);
    fireEvent.click(screen.getByText('...'));
    expect(onClick).toHaveBeenCalled();
  });
});
```

---

## ✅ Completion Checklist

```markdown
□ PHASE 1: Discovery complete
  □ Design analyzed, gaps resolved
  
□ PHASE 2: Extraction complete
  □ Properties extracted, mapped to tech

□ PHASE 3: Implementation complete
  □ Code injected 1:1 from design

□ PHASE 4: Verification complete
  □ Visual 1:1 match confirmed
  □ Interactions work
  □ Responsive behavior correct
  □ PM approved

□ PHASE 5: Polish complete
  □ Code optimized (if applicable)
  □ Documentation updated
  □ Tests added

□ FINAL:
  □ Quality gates passed
  □ Committed
```

---

## ⚠️ Common Pitfalls

**❌ DON'T:**
```typescript
// Inventing styles not in design
<div className="bg-gradient-to-r from-blue-400">  // Not in design!

// Using different colors "because better"
<button className="bg-green-500">  // Design said blue-500!

// Adding animations not in design
<div className="animate-bounce">  // Not specified!
```

**✅ DO:**
```typescript
// Use exact colors from design
<div className="bg-blue-500">  // From design extraction

// Use exact layout from design
<div className="flex flex-col gap-4">  // From design extraction

// If unsure, ask PM
// Q: Design doesn't show mobile layout. Should I:
//    A) Stack vertically
//    B) Wait for mobile design
```

---

## 📚 Related

- `meta-prompt.md` - Role & Mindset
- `think-first.md` - Planning
- `quality-gates.md` - Pre-commit checks
- `new-feature.md` - If designing from scratch
- `project-guide.md` - Project styling standards

**Remember:** UI Sync = INJECTION, not INVENTION. Match design exactly!
