from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import traceback

load_dotenv()

# Use mock for testing first
from ice_breaker import ice_break_with
# from ice_breaker import ice_break_with  # Uncomment this when API is fixed

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    try:
        name = request.form.get("name")
        print(f"Received name: {name}")
        
        if not name:
            return jsonify({"error": "Name is required"}), 400
        
        # Call your ice_break_with function
        summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(name=name)
        
        print("Summary:", summary_and_facts)
        print("Interests:", interests)
        print("Ice Breakers:", ice_breakers)
        print("Profile pic URL:", profile_pic_url)
        
        # Convert to dict and return
        result = {
            "summary_and_facts": summary_and_facts.to_dict() if hasattr(summary_and_facts, 'to_dict') else summary_and_facts,
            "interests": interests.to_dict() if hasattr(interests, 'to_dict') else interests,
            "ice_breakers": ice_breakers.to_dict() if hasattr(ice_breakers, 'to_dict') else ice_breakers,
            "picture_url": profile_pic_url,
        }
        
        print("Final result:", result)
        return jsonify(result)
        
    except Exception as e:
        print(f"Error in process route: {str(e)}")
        print("Traceback:", traceback.format_exc())
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)