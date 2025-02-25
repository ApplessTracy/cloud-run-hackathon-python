
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
import json
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
mylink = 'https://cloud-run-hackathon-python-ev2hwn2rma-uc.a.run.app'
playerUrl = []
playerDetail = []
playerX = []
playerY = []

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)

    data = request.json
    
    myX = data['arena']['dims'][0]
    myY = data['arena']['dims'][1]
    myFace = data['arena']['state'][mylink]['direction']
    isHit = data['arena']['state'][mylink]['wasHit']
    tempKey = []
    tempValue = []
    face = 'N'

    playerLocation = data['arena']['state']
    for key, value in playerLocation.items():
        tempKey = [key]
        tempValue = [value]
        playerUrl.append(tempKey)
        playerDetail.append(tempValue)
        playerX.append(tempValue[0]['x'])
        playerY.append(tempValue[0]['y'])
        
    for i in range(len(playerX)):
        if isHit:
            return moves[random.randrange(len(moves))]

        if playerY == myY:
            if playerX[i] < myX and myX-3 <= playerX[i]:
                
                if myFace == 'W':
                    return moves[1]
                else:
                    return moves[2]
            elif myX < playerX[i] and playerX[i] <= myX-3:
                if myFace == 'E':
                    return moves[1]
                else:
                    return moves[3]
        else:
            return moves[random.randrange(len(moves))]



if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
