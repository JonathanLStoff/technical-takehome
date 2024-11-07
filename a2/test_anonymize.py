import unittest
import anonymize

POSSIBLE_NAMES:list[str] = [
            "Alice", 
            "Bob", 
            "Charlie", 
            "Dr.", 
            "Prof.", 
            "Norman", 
            "Jeff", 
            "Jordan", 
            "St.", 
            "Augustine", 
            "Dave", 
            "Eve", 
        ]



class TestAnonymize(unittest.TestCase):
        
    def test_parta(self):
        # Test parta
        parta_input_text = [
            "Alice and Bob are talking to Charlie.", 
            "Alice, Bob, and Charlie went to the park.", 
            "Dr. Alice visited Prof. Bob at the university.", 
            "Norman and Jeff are talking to Jordan about going to the St. Augustine beach."
            ]
        for parta_input_text_str in parta_input_text:
            for name in POSSIBLE_NAMES:
                self.assertFalse(name in anonymize.anonymize_names_parta(parta_input_text_str))
    def test_partb(self):
        partb_test_strings = [
        "Alice and Bob are talking to Charlie about going to New York City.",
        "alice and bob are discussing with Charlie about visiting Los Angeles.",
        "Bob and Eve are planning a trip to paris next summer.",
        "Charlie and Alice met with Dave in San Francisco last week.",
        "eve and Charlie were excited about the event in Chicago.",
        "Charlie and Bob are thinking of moving to Tokyo soon.",
        "Alice and Dave went to see a show in London.",
        "Alice and Bob had dinner with Eve in Madrid.",
        "bob and Eve are going to Sydney for a conference.",
        "Charlie and Alice took a vacation in Rome.",
        "Charlie and Dave are considering a job offer in Berlin.",
        "eve and Charlie are visiting their friend in Amsterdam.",
        "Charlie and Bob are attending a wedding in Bangkok.",
        "Alice and Dave spent their holidays in Barcelona.",
        "Bob and Eve are looking for apartments in Vienna.",
        "Charlie and Dave are organizing an event in Prague.",
        "alice and Charlie are exploring opportunities in Dubai.",
        "Bob and Charlie are discussing their plans in Dublin.",
        "Alice and Bob are thinking about a trip to Vancouver.",
        "Charlie and Eve are preparing for a move to Montreal."
        ]
        for input_text in partb_test_strings:
            for name in POSSIBLE_NAMES:
                self.assertFalse(name in anonymize.anonymize_names_partb(input_text))
    
if __name__ == '__main__':
    unittest.main()