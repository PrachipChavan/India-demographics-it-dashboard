import pandas as pd
import os

def generate_csv():
    # Realistic data estimates for India's 28 states and 8 Union Territories
    data = [
        # States
        {"State/UT": "Andhra Pradesh", "Type": "State", "Population (Millions)": 53.2, "Literacy Rate (%)": 67.4, 
         "Primary Language": "Telugu", "Primary Share (%)": 89.1, "Secondary Language": "Urdu", "Secondary Share (%)": 6.9,
         "IT Companies": 450, "Major IT Hub": "Visakhapatnam", "Avg IT Salary (LPA)": 6.8},
        
        {"State/UT": "Arunachal Pradesh", "Type": "State", "Population (Millions)": 1.6, "Literacy Rate (%)": 65.4, 
         "Primary Language": "Nishi", "Primary Share (%)": 20.7, "Secondary Language": "Adi", "Secondary Share (%)": 17.3,
         "IT Companies": 10, "Major IT Hub": "Itanagar", "Avg IT Salary (LPA)": 4.5},
        
        {"State/UT": "Assam", "Type": "State", "Population (Millions)": 35.6, "Literacy Rate (%)": 72.2, 
         "Primary Language": "Assamese", "Primary Share (%)": 48.4, "Secondary Language": "Bengali", "Secondary Share (%)": 28.9,
         "IT Companies": 120, "Major IT Hub": "Guwahati", "Avg IT Salary (LPA)": 5.2},
         
        {"State/UT": "Bihar", "Type": "State", "Population (Millions)": 127.3, "Literacy Rate (%)": 61.8, 
         "Primary Language": "Hindi", "Primary Share (%)": 78.0, "Secondary Language": "Maithili", "Secondary Share (%)": 12.5,
         "IT Companies": 80, "Major IT Hub": "Patna", "Avg IT Salary (LPA)": 4.8},
         
        {"State/UT": "Chhattisgarh", "Type": "State", "Population (Millions)": 29.4, "Literacy Rate (%)": 70.3, 
         "Primary Language": "Chhattisgarhi", "Primary Share (%)": 62.0, "Secondary Language": "Hindi", "Secondary Share (%)": 34.0,
         "IT Companies": 150, "Major IT Hub": "Raipur", "Avg IT Salary (LPA)": 5.0},
         
        {"State/UT": "Goa", "Type": "State", "Population (Millions)": 1.6, "Literacy Rate (%)": 88.7, 
         "Primary Language": "Konkani", "Primary Share (%)": 66.1, "Secondary Language": "Marathi", "Secondary Share (%)": 10.9,
         "IT Companies": 180, "Major IT Hub": "Panaji", "Avg IT Salary (LPA)": 6.5},
         
        {"State/UT": "Gujarat", "Type": "State", "Population (Millions)": 63.8, "Literacy Rate (%)": 78.0, 
         "Primary Language": "Gujarati", "Primary Share (%)": 85.5, "Secondary Language": "Hindi", "Secondary Share (%)": 7.2,
         "IT Companies": 1800, "Major IT Hub": "Ahmedabad/GIFT City", "Avg IT Salary (LPA)": 7.5},
         
        {"State/UT": "Haryana", "Type": "State", "Population (Millions)": 28.2, "Literacy Rate (%)": 75.6, 
         "Primary Language": "Hindi", "Primary Share (%)": 87.3, "Secondary Language": "Punjabi", "Secondary Share (%)": 9.5,
         "IT Companies": 2900, "Major IT Hub": "Gurugram", "Avg IT Salary (LPA)": 9.8},
         
        {"State/UT": "Himachal Pradesh", "Type": "State", "Population (Millions)": 7.4, "Literacy Rate (%)": 82.8, 
         "Primary Language": "Pahari", "Primary Share (%)": 36.6, "Secondary Language": "Hindi", "Secondary Share (%)": 35.0,
         "IT Companies": 90, "Major IT Hub": "Shimla", "Avg IT Salary (LPA)": 5.5},
         
        {"State/UT": "Jharkhand", "Type": "State", "Population (Millions)": 38.5, "Literacy Rate (%)": 66.4, 
         "Primary Language": "Hindi", "Primary Share (%)": 57.6, "Secondary Language": "Santhali", "Secondary Share (%)": 9.9,
         "IT Companies": 140, "Major IT Hub": "Ranchi", "Avg IT Salary (LPA)": 5.1},
         
        {"State/UT": "Karnataka", "Type": "State", "Population (Millions)": 67.6, "Literacy Rate (%)": 75.4, 
         "Primary Language": "Kannada", "Primary Share (%)": 66.3, "Secondary Language": "Urdu", "Secondary Share (%)": 10.5,
         "IT Companies": 5200, "Major IT Hub": "Bengaluru", "Avg IT Salary (LPA)": 11.2},
         
        {"State/UT": "Kerala", "Type": "State", "Population (Millions)": 35.7, "Literacy Rate (%)": 94.0, 
         "Primary Language": "Malayalam", "Primary Share (%)": 97.0, "Secondary Language": "Tamil", "Secondary Share (%)": 2.1,
         "IT Companies": 950, "Major IT Hub": "Kochi/Thiruvananthapuram", "Avg IT Salary (LPA)": 7.2},
         
        {"State/UT": "Madhya Pradesh", "Type": "State", "Population (Millions)": 85.4, "Literacy Rate (%)": 69.3, 
         "Primary Language": "Hindi", "Primary Share (%)": 87.3, "Secondary Language": "Bhili", "Secondary Share (%)": 4.9,
         "IT Companies": 650, "Major IT Hub": "Indore", "Avg IT Salary (LPA)": 6.2},
         
        {"State/UT": "Maharashtra", "Type": "State", "Population (Millions)": 123.1, "Literacy Rate (%)": 82.3, 
         "Primary Language": "Marathi", "Primary Share (%)": 68.9, "Secondary Language": "Hindi", "Secondary Share (%)": 12.9,
         "IT Companies": 4400, "Major IT Hub": "Mumbai/Pune", "Avg IT Salary (LPA)": 10.5},
         
        {"State/UT": "Manipur", "Type": "State", "Population (Millions)": 3.0, "Literacy Rate (%)": 76.9, 
         "Primary Language": "Manipuri", "Primary Share (%)": 53.3, "Secondary Language": "Mao", "Secondary Share (%)": 7.5,
         "IT Companies": 25, "Major IT Hub": "Imphal", "Avg IT Salary (LPA)": 4.6},
         
        {"State/UT": "Meghalaya", "Type": "State", "Population (Millions)": 3.3, "Literacy Rate (%)": 74.4, 
         "Primary Language": "Khasi", "Primary Share (%)": 47.1, "Secondary Language": "Garo", "Secondary Share (%)": 33.7,
         "IT Companies": 30, "Major IT Hub": "Shillong", "Avg IT Salary (LPA)": 4.8},
         
        {"State/UT": "Mizoram", "Type": "State", "Population (Millions)": 1.2, "Literacy Rate (%)": 91.3, 
         "Primary Language": "Mizo", "Primary Share (%)": 73.2, "Secondary Language": "English", "Secondary Share (%)": 10.5,
         "IT Companies": 15, "Major IT Hub": "Aizawl", "Avg IT Salary (LPA)": 4.4},
         
        {"State/UT": "Nagaland", "Type": "State", "Population (Millions)": 2.2, "Literacy Rate (%)": 79.6, 
         "Primary Language": "Konyak", "Primary Share (%)": 13.5, "Secondary Language": "Ao", "Secondary Share (%)": 12.0,
         "IT Companies": 20, "Major IT Hub": "Kohima", "Avg IT Salary (LPA)": 4.5},
         
        {"State/UT": "Odisha", "Type": "State", "Population (Millions)": 46.2, "Literacy Rate (%)": 72.9, 
         "Primary Language": "Odia", "Primary Share (%)": 82.7, "Secondary Language": "Hindi", "Secondary Share (%)": 2.9,
         "IT Companies": 380, "Major IT Hub": "Bhubaneswar", "Avg IT Salary (LPA)": 6.4},
         
        {"State/UT": "Punjab", "Type": "State", "Population (Millions)": 30.1, "Literacy Rate (%)": 75.8, 
         "Primary Language": "Punjabi", "Primary Share (%)": 89.8, "Secondary Language": "Hindi", "Secondary Share (%)": 7.6,
         "IT Companies": 620, "Major IT Hub": "Mohali", "Avg IT Salary (LPA)": 7.0},
         
        {"State/UT": "Rajasthan", "Type": "State", "Population (Millions)": 81.0, "Literacy Rate (%)": 66.1, 
         "Primary Language": "Hindi", "Primary Share (%)": 89.4, "Secondary Language": "Bhili", "Secondary Share (%)": 4.6,
         "IT Companies": 750, "Major IT Hub": "Jaipur", "Avg IT Salary (LPA)": 6.8},
         
        {"State/UT": "Sikkim", "Type": "State", "Population (Millions)": 0.7, "Literacy Rate (%)": 81.4, 
         "Primary Language": "Nepali", "Primary Share (%)": 62.6, "Secondary Language": "Sikkimese", "Secondary Share (%)": 7.7,
         "IT Companies": 15, "Major IT Hub": "Gangtok", "Avg IT Salary (LPA)": 4.8},
         
        {"State/UT": "Tamil Nadu", "Type": "State", "Population (Millions)": 76.5, "Literacy Rate (%)": 80.1, 
         "Primary Language": "Tamil", "Primary Share (%)": 89.4, "Secondary Language": "Telugu", "Secondary Share (%)": 5.7,
         "IT Companies": 3400, "Major IT Hub": "Chennai/Coimbatore", "Avg IT Salary (LPA)": 9.5},
         
        {"State/UT": "Telangana", "Type": "State", "Population (Millions)": 38.0, "Literacy Rate (%)": 72.8, 
         "Primary Language": "Telugu", "Primary Share (%)": 75.4, "Secondary Language": "Urdu", "Secondary Share (%)": 12.2,
         "IT Companies": 3100, "Major IT Hub": "Hyderabad", "Avg IT Salary (LPA)": 10.2},
         
        {"State/UT": "Tripura", "Type": "State", "Population (Millions)": 4.1, "Literacy Rate (%)": 87.2, 
         "Primary Language": "Bengali", "Primary Share (%)": 65.7, "Secondary Language": "Kokborok", "Secondary Share (%)": 26.2,
         "IT Companies": 40, "Major IT Hub": "Agartala", "Avg IT Salary (LPA)": 4.9},
         
        {"State/UT": "Uttar Pradesh", "Type": "State", "Population (Millions)": 235.0, "Literacy Rate (%)": 67.7, 
         "Primary Language": "Hindi", "Primary Share (%)": 94.1, "Secondary Language": "Urdu", "Secondary Share (%)": 5.4,
         "IT Companies": 2100, "Major IT Hub": "Noida/Greater Noida", "Avg IT Salary (LPA)": 9.0},
         
        {"State/UT": "Uttarakhand", "Type": "State", "Population (Millions)": 11.4, "Literacy Rate (%)": 78.8, 
         "Primary Language": "Hindi", "Primary Share (%)": 88.0, "Secondary Language": "Urdu", "Secondary Share (%)": 4.2,
         "IT Companies": 160, "Major IT Hub": "Dehradun", "Avg IT Salary (LPA)": 6.0},
         
        {"State/UT": "West Bengal", "Type": "State", "Population (Millions)": 99.1, "Literacy Rate (%)": 76.3, 
         "Primary Language": "Bengali", "Primary Share (%)": 86.2, "Secondary Language": "Hindi", "Secondary Share (%)": 7.0,
         "IT Companies": 1100, "Major IT Hub": "Kolkata", "Avg IT Salary (LPA)": 8.0},
         
        # Union Territories
        {"State/UT": "Andaman and Nicobar Islands", "Type": "UT", "Population (Millions)": 0.4, "Literacy Rate (%)": 86.6, 
         "Primary Language": "Bengali", "Primary Share (%)": 28.5, "Secondary Language": "Tamil", "Secondary Share (%)": 15.2,
         "IT Companies": 5, "Major IT Hub": "Port Blair", "Avg IT Salary (LPA)": 4.5},
         
        {"State/UT": "Chandigarh", "Type": "UT", "Population (Millions)": 1.2, "Literacy Rate (%)": 86.0, 
         "Primary Language": "Hindi", "Primary Share (%)": 67.5, "Secondary Language": "Punjabi", "Secondary Share (%)": 27.9,
         "IT Companies": 350, "Major IT Hub": "Chandigarh", "Avg IT Salary (LPA)": 7.8},
         
        {"State/UT": "Dadra and Nagar Haveli and Daman and Diu", "Type": "UT", "Population (Millions)": 0.6, "Literacy Rate (%)": 77.2, 
         "Primary Language": "Gujarati", "Primary Share (%)": 53.5, "Secondary Language": "Hindi", "Secondary Share (%)": 26.2,
         "IT Companies": 30, "Major IT Hub": "Daman", "Avg IT Salary (LPA)": 5.5},
         
        {"State/UT": "Delhi", "Type": "UT", "Population (Millions)": 21.2, "Literacy Rate (%)": 86.2, 
         "Primary Language": "Hindi", "Primary Share (%)": 81.3, "Secondary Language": "Punjabi", "Secondary Share (%)": 6.0,
         "IT Companies": 2200, "Major IT Hub": "New Delhi/Okhla", "Avg IT Salary (LPA)": 9.5},
         
        {"State/UT": "Jammu and Kashmir", "Type": "UT", "Population (Millions)": 13.6, "Literacy Rate (%)": 67.2, 
         "Primary Language": "Kashmiri", "Primary Share (%)": 53.3, "Secondary Language": "Dogri", "Secondary Share (%)": 20.0,
         "IT Companies": 110, "Major IT Hub": "Srinagar/Jammu", "Avg IT Salary (LPA)": 5.4},
         
        {"State/UT": "Ladakh", "Type": "UT", "Population (Millions)": 0.3, "Literacy Rate (%)": 77.2, 
         "Primary Language": "Ladakhi", "Primary Share (%)": 39.0, "Secondary Language": "Balti", "Secondary Share (%)": 18.0,
         "IT Companies": 2, "Major IT Hub": "Leh", "Avg IT Salary (LPA)": 4.2},
         
        {"State/UT": "Lakshadweep", "Type": "UT", "Population (Millions)": 0.07, "Literacy Rate (%)": 91.8, 
         "Primary Language": "Malayalam", "Primary Share (%)": 84.1, "Secondary Language": "Dhivehi", "Secondary Share (%)": 15.6,
         "IT Companies": 1, "Major IT Hub": "Kavaratti", "Avg IT Salary (LPA)": 4.0},
         
        {"State/UT": "Puducherry", "Type": "UT", "Population (Millions)": 1.6, "Literacy Rate (%)": 85.8, 
         "Primary Language": "Tamil", "Primary Share (%)": 88.2, "Secondary Language": "Telugu", "Secondary Share (%)": 6.0,
         "IT Companies": 70, "Major IT Hub": "Puducherry", "Avg IT Salary (LPA)": 6.0}
    ]
    
    df = pd.DataFrame(data)
    
    # Ensure directory exists
    target_dir = "C:\\Users\\Prachi\\OneDrive\\Desktop\\topmentor\\india_dashboard"
    os.makedirs(target_dir, exist_ok=True)
    
    # Save CSV
    filepath = os.path.join(target_dir, "india_demographics.csv")
    df.to_csv(filepath, index=False)
    print(f"Data saved successfully to {filepath}")

if __name__ == "__main__":
    generate_csv()
