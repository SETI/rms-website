var config = {
	host: "https://pds.nasa.gov",	// Email Server Host
	feedback: {
		header: "Ring-Moon Systems Feedback and Support",
		feedbackType: "Comment,Question,Problem/Bug,Kudos,Other",
		additionalLinks: [
            {
				title: "PDS-Wide Search",
				url: "https://pds.nasa.gov/datasearch/data-search/"
			},
            {
				title: "Browse Data Volumes",
				url: "https://pds-rings.seti.org/viewmaster/volumes/"
			},
            {
				title: "OPUS Search",
				url: "https://opus.pds-rings.seti.org/opus/#"
			},
		]
	},
	tab: {
		label: "Questions / Feedback",		// default: Need Help?
        // OPUS - moved directly into feedback.css
        // color: "#000000",
		// fontColor: "#ffffffc0",		// default: #ffffff
		fontSize: "13",				// default: 16
		size: {
			width: "185",			// default: 150
			height: "35"			// default: 60
		},
		placement: {
			side: "right",			// default: right
			offset: "50"			// default: 50
		}
	}
};
