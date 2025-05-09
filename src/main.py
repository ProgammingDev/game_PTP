from app import create_app

app = create_app()


for rule in app.url_map.iter_rules():
    methods = ", ".join(sorted(rule.methods - {'HEAD', 'OPTIONS'}))
    print(f"{rule.endpoint:30s} {methods:15s} {rule.rule}")

if __name__ == '__main__':
   
    app.run(debug=True,port=4000)