Test case scenarios
	Flow 1
		Buyer selects an item/ fulfillment for raising a complaint, buyer app creates a complaint (/issue) & seller app marks the issue as processing (on_issue)
		Seller app seeks more information (for example, more images) for providing a resolution on the complaint (unsolicited /on_issue)
		Buyer app asks the same to the buyer and the buyer provides the required information (for example, provides more images). This is then sent to the seller app (/issue) 
		The seller receives the information and processes the same (/on_issue)
		Buyer app checks for a status update on the complaint (issue_status) and seller app responds with current state and the action trail of the complaint (on_issue_status)
		The seller app then proposes two resolution options (example, refund or replacement), providing their GRO information, to the buyer app (unsolicited on_issue) 
		Buyer accepts one of the resolution and the buyer app sends the same to the seller app (/issue)
		Seller app then resolves the complaint with the selected resolution (/on_issue) and takes necessary action (for example, /update call with relevant issue_id)
		Buyer closes the complaint and provides a rating to the resolution, buyer app sends this to the seller app marking the complaint as closed (/issue) 