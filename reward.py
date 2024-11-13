def reward_function(params):
    '''
    Reward function that calculates reward based on lane adherence
    and distance to obstacles.
    '''

    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    distance_to_closest_obstacle = params['objects_distance'][params['closest_objects'][1]]

    # Initialize reward values
    reward = 1e-3
    reward_lane = 1
    reward_avoid = 1

    # Reward lane logic
    if distance_from_center < 0.35 * track_width:
        reward_lane = 1
    elif distance_from_center < 0.5 * track_width:
        reward_lane = 3.33 * track_width - 6.66 * track_width * distance_from_center
    else:
        reward_lane = 1e-3

    # Reward avoid logic
    if distance_to_closest_obstacle < 0.15:
        reward_avoid = 1e-3
    elif 0.15 <= distance_to_closest_obstacle < 0.3:
        reward_avoid = (distance_to_closest_obstacle - 0.25) * 4 + 1e-3
    else:
        reward_avoid = 1

    # Final reward calculation
    reward = reward_lane * 1 + reward_avoid * 2.5

    return reward