
function login(username, password) {
	$.ajax({
		url: "queries/login",
		type: "POST",
		data: {
			username: username,
			password: password
		},
		success: function(string) {
			if (string === "failure") {
				alert('FAIL');
			} else {
				$('body').html(string);
			}
		}
	});
}

function logout() {
	$.ajax({
		url: "queries/logout",
		type: "POST",
		data: {},
		success: function(string) {
			$('body').html(string);
		}
	});
}

function register(form) {
	form.find(".username").css('border-color', 'initial');
	form.find(".password").css('border-color', 'initial');
	form.find(".repassword").css('border-color', 'initial');

	form.find(".error-username").css('display', 'none')
	form.find(".error-password").css('display', 'none')
	form.find(".error-repassword").css('display', 'none')

	var username = $(form.find(".username")).val();
	var password = $(form.find(".password")).val();
	var repassword = $(form.find(".repassword")).val();
	var email = $(form.find(".email")).val();

	var error = false;
	if (username == '') {
		form.find(".username").css('border-color', 'red');
		form.find(".error-username").css('display', 'initial');
		form.find(".error-username").html('Skriv ett användar namn<br>');
		error = true;
	}
	if (password == '') {
		form.find(".password").css('border-color', 'red');
		form.find(".error-password").css('display', 'initial');
		error = true;
	}
	if (password != repassword) {
		form.find(".repassword").css('border-color', 'red');
		form.find(".error-repassword").css('display', 'initial');
		error = true;
	}
	if (error) return;

	$(".register-div .spinner").css("display", "inline-block");
	$(".register-div form").css("display", "none");

	$.ajax({
		url: "queries/register",
		type: "POST",
		data: {
			username: username,
			password: password,
			email: email
		},
		success: function(string) {
			$(".register-div .spinner").css("display", "none");
			$(".register-div form").css("display", "inline-block");
			
			if (string === "error") {
				form.find(".error-username").css('display', 'initial');
				form.find(".error-username").html('Användar namnet används redan<br>');
			} else {
				$('body').html(string);
			}
		}
	});
	
	return false;
}