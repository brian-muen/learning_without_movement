"""
This script is for generating JSON target files directly, which is the form used in the experiment. 
To implement target jump, clamp, or online feedback make appropriate changes in the area flagged by the **TODO** comment.
"""
import json
import random

def generateTargetAngles(numTargets):
    """
    temporary usage of this function for non-evenly spaced targets
    """
    angleList = [45, 135]
    if (len(angleList) != numTargets):
        raise Exception('Target file does not have the right amount of targets. Should have ' + str(numTargets) + ' targets, but only has ' + str(len(angleList)))
    
    return angleList

def generateJSON(numTargets, numTrials, rotationConditions):
    """
    Generate target file with proper triplet structure and rotation conditions
    
    Args:
        numTargets: Number of target positions (should be 4)
        numTrials: Total number of trials
        rotationConditions: List of rotation conditions [0, 15, -15]
    """
    if numTargets != 4:
        raise ValueError(f"Expected 4 target positions, got {numTargets}")
    
    # Fixed target angles
    targetAngles = [45, 135, 225, 315]
    
    # Ensure we have the correct number of rotation conditions
    if len(rotationConditions) != 3:
        raise ValueError(f"Expected 3 rotation conditions, got {len(rotationConditions)}")
    
    # Calculate number of triplets
    numTriplets = numTrials // 3
    
    # Initialize trial data
    trials = []
    
    # Generate trials in triplets
    for triplet_idx in range(numTriplets):
        # Randomly select rotation condition for middle trial
        rotation = random.choice(rotationConditions)
        
        # Randomly select target angle
        target_angle = random.choice(targetAngles)
        
        # First trial (flanker) - movement trial with no rotation
        trials.append({
            "triplet_id": triplet_idx,
            "trial_position": 1,
            "triplet_type": "movement",
            "rotation_condition": 0,
            "target_angle": target_angle
        })
        
        # Second trial (middle) - either movement or no-movement
        trial_type = random.choice(["movement", "no-movement"])
        trials.append({
            "triplet_id": triplet_idx,
            "trial_position": 2,
            "triplet_type": trial_type,
            "rotation_condition": rotation,
            "target_angle": target_angle
        })
        
        # Third trial (flanker) - movement trial with no rotation
        trials.append({
            "triplet_id": triplet_idx,
            "trial_position": 3,
            "triplet_type": "movement",
            "rotation_condition": 0,
            "target_angle": target_angle
        })
    
    # Convert to JSON
    jsonData = {
        "trials": trials,
        "numtrials": numTrials,
        "target_distance": 250,  # Fixed target distance
        "rotation_conditions": rotationConditions
    }
    
    return jsonData

if __name__ == "__main__":
    # Generate test file with 12 trials (4 triplets)
    numTrials = 12
    rotationConditions = [0, 15, -15]
    
    # Generate JSON
    jsonData = generateJSON(4, numTrials, rotationConditions)
    
    # Save to file
    with open('testShort.json', 'w') as f:
        json.dump(jsonData, f, indent=4)
    
    print(f"Generated test file with {numTrials} trials")
    


