> [!TIP] In fast API, the route order matters.

**Example**
```python
# ✅ CORRECT ORDER (specific → general)
@router.get("/travel/visa-info/db/all")                               # Most specific
@router.get("/travel/visa-info/db/destination/{destination_country}") # Specific  
@router.get("/travel/visa-info/db/origin/{origin_country}")           # Specific
@router.get("/travel/visa-info/db/{origin_country}/{destination_country}") # General (catch-all)
```