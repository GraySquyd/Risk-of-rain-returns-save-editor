from flask import Flask, render_template, request
from flask import send_from_directory
import os

app = Flask(__name__)

def read_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None

def insert_after_keyword(source_file, destination_file, keyword, new_string):
    try:
        with open(source_file, 'a') as file:
            file.write("")  # Write an empty string to create the file

        with open(source_file, 'r') as file:
            source_content = file.read()

        index_keyword = source_content.find(keyword)

        if index_keyword != -1:
            modified_content = (
                source_content[:index_keyword + len(keyword)] +
                new_string +
                source_content[index_keyword + len(keyword):]
            )

            with open(destination_file, 'w') as file:
                file.write(modified_content)
            print("Operation successful: The file content has been inserted after the keyword.")
        else:
            print("Keyword not found in the source file.")
    except FileNotFoundError:
        print(f"The file {source_file} could not be created or found.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error="No file selected.")
    
    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error="No file selected.")

    source_file = os.path.join('uploads', file.filename)
    file.save(source_file)

    destination_folder = request.form.get('destination_folder')
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    keyword = '"flags":['

    file_content = read_file_content(source_file)

    if file_content is not None:
        destination_file = os.path.join(destination_folder, 'save.json')
        new_string = '"challenge_unlock_engineer_completed","challenge_unlock_enforcer_completed","challenge_unlock_bandit_completed","challenge_unlock_hand_completed","challenge_unlock_miner_completed","challenge_unlock_sniper_completed","challenge_unlock_acrid_completed","challenge_unlock_mercenary_completed","challenge_unlock_loader_completed","challenge_unlock_chef_completed","challenge_unlock_pilot_completed","challenge_unlock_drifter_completed","challenge_unlock_arti_completed","challenge_unlock_engi_x2_completed","challenge_unlock_engi_c2_completed","challenge_unlock_engi_v2_completed","challenge_unlock_enforcer_z2_completed","challenge_unlock_enforcer_x2_completed","challenge_unlock_enforcer_v2_completed","challenge_unlock_bandit_z2_completed","challenge_unlock_bandit_c2_completed","challenge_unlock_bandit_v2_completed","challenge_unlock_hand_x2_completed","challenge_unlock_hand_x3_completed","challenge_unlock_hand_v2_completed","challenge_unlock_miner_z2_completed","challenge_unlock_miner_x2_completed","challenge_unlock_miner_c2_completed","challenge_unlock_sniper_z2_completed","challenge_unlock_sniper_x2_completed","challenge_unlock_sniper_c2_completed","challenge_unlock_acrid_z2_completed","challenge_unlock_acrid_x2_completed","challenge_unlock_acrid_c2_completed","challenge_unlock_mercenary_x2_completed","challenge_unlock_mercenary_c2_completed","challenge_unlock_mercenary_v2_completed","challenge_unlock_loader_z2_completed","challenge_unlock_loader_x2_completed","challenge_unlock_loader_v2_completed","challenge_unlock_chef_z2_completed","challenge_unlock_chef_c2_completed","challenge_unlock_chef_v2_completed","challenge_unlock_pilot_z2_completed","challenge_unlock_pilot_c2_completed","challenge_unlock_pilot_v2_completed","challenge_unlock_drifter_x2_completed","challenge_unlock_drifter_c2_completed","challenge_unlock_drifter_v2_completed","challenge_unlock_arti_x2_completed","challenge_unlock_arti_c2_completed","challenge_unlock_arti_v2_completed","challenge_unlock_commando_skin_a_completed","challenge_unlock_enforcer_skin_a_completed","challenge_unlock_hand_skin_a_completed","challenge_unlock_miner_skin_a_completed","challenge_unlock_sniper_skin_a_completed","challenge_unlock_pilot_skin_a_completed","challenge_unlock_huntress_skin_s_completed","challenge_unlock_commando_skin_s_completed","challenge_unlock_enforcer_skin_s_completed","challenge_unlock_bandit_skin_s_completed","challenge_unlock_acrid_skin_s_completed","challenge_unlock_mercenary_skin_s_completed","challenge_unlock_loader_skin_s_completed","challenge_unlock_chef_skin_s_completed","challenge_unlock_arti_skin_s_completed","challenge_unlock_drifter_skin_s_completed","challenge_unlock_artifact_honor_completed","challenge_unlock_artifact_kin_completed","challenge_unlock_artifact_distortion_completed","challenge_unlock_artifact_spite_completed","challenge_unlock_artifact_glass_completed","challenge_unlock_artifact_enigma_completed","challenge_unlock_artifact_sacrifice_completed","challenge_unlock_artifact_command_completed","challenge_unlock_artifact_spirit_completed","challenge_unlock_artifact_origin_completed","challenge_unlock_artifact_mountain_completed","challenge_unlock_artifact_dissonance_completed","challenge_unlock_artifact_temporary_completed","challenge_unlock_artifact_cognation_completed",'


        insert_after_keyword(source_file, destination_file, keyword, new_string)

        return render_template('index.html', success="Operation successful: The file content has been inserted after the keyword.")
    else:
        return render_template('index.html', error="Error reading the file.")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
