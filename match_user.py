def match_users_based_on_interests(users, interests):
  """
  Matches users based on their interests.

  Args:
    users: A list of users, where each user is represented as a dictionary with the following keys:
      * id: The user's ID.
      * interests: A list of the user's interests.
    interests: A list of interests.

  Returns:
    A list of tuples, where each tuple contains the IDs of two matched users.
  """

  # Create a dictionary to store the match scores for each user pair.
  match_scores = {}

  # Iterate over all user pairs.
  for user1 in users:
    for user2 in users:
      if user1["id"] != user2["id"]:
        # Calculate the match score for the user pair.
        match_score = calculate_match_score(user1["interests"], user2["interests"])

        # Store the match score in the dictionary.
        match_scores[(user1["id"], user2["id"])] = match_score

  # Sort the match scores in descending order.
  sorted_match_scores = sorted(match_scores.items(), key=lambda x: x[1], reverse=True)

  # Create a list to store the matched user pairs.
  matched_user_pairs = []

  # Iterate over the sorted match scores.
  for match_score in sorted_match_scores:
    user_pair = match_score[0]

    # Add the matched user pair to the list.
    matched_user_pairs.append(user_pair)

  # Return the list of matched user pairs.
  return matched_user_pairs

def calculate_match_score(user1_interests, user2_interests):
  """
  Calculates the match score for two users.

  Args:
    user1_interests: A list of the first user's interests.
    user2_interests: A list of the second user's interests.

  Returns:
    A float representing the match score for the two users.
  """

  # Calculate the number of common interests.
  num_common_interests = len(set(user1_interests) & set(user2_interests))

  # Calculate the match score.
  match_score = num_common_interests / (len(user1_interests) + len(user2_interests) - num_common_interests)

  # Return the match score.
  return match_score