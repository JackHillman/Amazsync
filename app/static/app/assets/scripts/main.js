Buddy.init("bbbbbc.cJtLKKDtdpNfc", "2b58d12f-1cff-0380-11d8-689ce04c415e" );

var newProject;

function formToggle() {
	$('.form-container').toggleClass('hidden');
}

var projectData = new Vue();

function initProject(path) {
	formToggle();

	new Vue({
		el: '#init-form',
		data: {
			name: "",
			description: "",
			created: new Date().toLocaleDateString(),
			type: "HTML",
			path: path,
			label: 'Initialise',
			existing: false
		}
	});
}

function editProject(path) {
	$.get('app/project/', {path: path}, function(data) {

		new Vue ({
			el: '#init-form',
			data: {
				name: data.name,
				description: data.description,
				created: data.created,
				type: data.type,
				path: data.path,
				label: 'Save',
				existing: true
			}
		});
	});

  formToggle();
}

function openProject(path) {
	$.get('app/project/', {path: path}, function(project) {
		// Post open project event
		Buddy.post('/metrics/events/openprojectdebug',
			{
				timeoutInSeconds: 30,
				value: {
					name: project.name,
					description: project.description,
					type: project.type
				}
			},
			// Log event details
			function(err, result) {
				if (!result.success) {
					console.log(err);
				} else {
					console.log("Successfully posted metric event for " + project.name);
				}
			}
		);
	});
}

$(document).ready(function() {
	$('.close-button').click(function() {
		formToggle();
	});
});

// buddy
