document.addEventListener(
    'DOMContentLoaded',
    function () {

        const successCard = document.getElementById(
            'successCard'
        );

        if (successCard) {

            setTimeout(function () {

                window.location.href = "/jobs/";

            }, 2000);

        }

        const applyForm = document.getElementById(
            'applyForm'
        );

        const applyBtn = document.getElementById(
            'applyBtn'
        );

        if (applyForm && applyBtn) {

            applyForm.addEventListener(
                'submit',
                function () {

                    applyBtn.innerHTML = `
                        <span class="spinner-border spinner-border-sm me-2"></span>
                        Applying...
                    `;

                    applyBtn.disabled = true;

                }
            );

        }

        const saveJobBtn = document.getElementById(
            'saveJobBtn'
        );

        if (saveJobBtn) {

            saveJobBtn.addEventListener(
                'click',
                function () {

                    const jobId = this.dataset.jobId;

                    saveJobBtn.innerText = 'Saving...';

                    saveJobBtn.disabled = true;

                    fetch(`/applications/save/${jobId}/`)
                        .then(response => {

                            if (response.ok) {

                                setTimeout(() => {

                                    saveJobBtn.innerText = 'Saved ✅';

                                    saveJobBtn.classList.remove(
                                        'btn-outline-dark'
                                    );

                                    saveJobBtn.classList.add(
                                        'btn-success'
                                    );

                                    saveJobBtn.disabled = false;

                                }, 700);

                            }

                        });

                }
            );

        }

    }
);


function showToast(message, type='success') {

    const toastBox = document.getElementById(
        'toastBox'
    );

    const toast = document.createElement(
        'div'
    );

    toast.className =
        `alert alert-${type} shadow-sm mb-2`;

    toast.innerText = message;

    toastBox.appendChild(toast);

    setTimeout(() => {

        toast.remove();

    }, 3000);

}