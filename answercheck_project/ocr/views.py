from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExamImageForm  # Import the form to handle image uploads

def upload_answer(request):
    form = ExamImageForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST' and form.is_valid():
        # Handle image upload
        exam_image = form.cleaned_data['exam_image']
        
        # Process the image (perform OCR logic here)
        # For now, we return the name of the uploaded image
        return HttpResponse(f'Image uploaded: {exam_image.name}')
    
    return render(request, 'upload_answer.html', {'form': form})
