from app import app, db
from models import PortfolioData

def seed_portfolio_data():
    with app.app_context():
        # Clear existing data
        PortfolioData.query.delete()
        
        # Add sample portfolio data
        sample_data = [
            PortfolioData(asset_name="Apple Inc.", asset_value=10000, asset_type="Stock"),
            PortfolioData(asset_name="Microsoft Corp.", asset_value=8000, asset_type="Stock"),
            PortfolioData(asset_name="US Treasury Bond", asset_value=5000, asset_type="Bond"),
            PortfolioData(asset_name="Real Estate Fund", asset_value=7000, asset_type="Real Estate"),
            PortfolioData(asset_name="Gold ETF", asset_value=3000, asset_type="Commodity")
        ]
        
        db.session.add_all(sample_data)
        db.session.commit()
        
        print("Sample portfolio data added successfully.")

if __name__ == "__main__":
    seed_portfolio_data()
