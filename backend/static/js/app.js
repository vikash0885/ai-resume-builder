document.addEventListener('DOMContentLoaded', () => {
    console.log('ResumeBuilder App Initialized');

    const generateBtn = document.getElementById('generateBtn');

    if (generateBtn) {
        generateBtn.addEventListener('click', async () => {
            const btnText = generateBtn.querySelector('span');
            const loadingIcon = document.getElementById('loadingIcon');

            // Loading state
            btnText.textContent = 'Generating...';
            loadingIcon.classList.remove('hidden');
            generateBtn.disabled = true;

            // Collect form data
            const formData = new FormData();
            document.querySelectorAll('input, textarea').forEach(input => {
                formData.append(input.name || input.placeholder, input.value);
            });

            // For now, let's just polish the experience field as a demo
            const experienceText = document.querySelector('textarea').value;

            try {
                const response = await fetch('/api/resumes/polish', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: experienceText })
                });

                const data = await response.json();

                if (data.polished_text) {
                    // Update the dashboard/preview with polished text
                    const preview = document.getElementById('resumePreview');
                    preview.innerHTML = `
                        <div class="space-y-6">
                            <h1 class="text-3xl font-bold text-gray-900">${document.querySelector('input[name="full_name"]').value || 'Your Name'}</h1>
                            <div class="text-gray-600">
                                ${document.querySelector('input[name="email"]').value} | 
                                ${document.querySelector('input[name="phone"]').value}
                            </div>
                            
                            <hr>
                            
                            <h2 class="text-xl font-bold text-primary">Experience</h2>
                            <div class="prose max-w-none">
                                <p class="whitespace-pre-wrap">${data.polished_text}</p>
                            </div>
                        </div>
                     `;
                    alert('Resume Generated with AI Polish!');

                    // Auto-save the resume
                    try {
                        const saveResponse = await fetch('/api/resumes/', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({
                                full_name: document.querySelector('input[name="full_name"]').value,
                                email: document.querySelector('input[name="email"]').value,
                                phone: document.querySelector('input[name="phone"]').value,
                                experience_raw: experienceText,
                                polished_experience: data.polished_text
                            })
                        });
                        console.log('Resume saved:', await saveResponse.json());
                    } catch (e) {
                        console.error("Save failed", e);
                    }
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Failed to generate resume. Is the backend running?');
            } finally {
                btnText.textContent = 'Generate & AI Polish';
                loadingIcon.classList.add('hidden');
                generateBtn.disabled = false;
            }
        });
    }
});
