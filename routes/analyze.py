from fastapi import APIRouter, HTTPException, Header
from services.scraper import get_market_data
from services.ai_analysis import analyze_data

router = APIRouter()

@router.get("/analyze/{sector}")
async def analyze_sector(sector: str, authorization: str = Header("mysecrettoken")):
    
    # Check token
    if authorization != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        data = get_market_data(sector)

        if not data:
            
            
            data = [
                f"{sector} sector is growing in India",
                "Market demand is increasing",
                "New startups are entering the market"
            ]

        report = analyze_data(sector, data)

        return {
            "sector": sector,
            "report": report
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
