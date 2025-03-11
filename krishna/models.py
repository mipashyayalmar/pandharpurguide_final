from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal



# Create your models here.
class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="krishna")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="maharashtra")
    country = models.CharField(max_length=50,default="india")
    def __str__(self):
        return self.name



class Rooms(models.Model):
    ROOM_STATUS = (
        ("1", "available"),
        ("2", "not available"),
    )

    ROOM_TYPE = (
        ("1", "premium"),
        ("2", "deluxe"),
        ("3", "basic"),
    )

    # Room details
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])  # Minimum 1 occupant
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Supports larger and precise pricing
    size = models.IntegerField(help_text="Room size in square feet")
    hotel = models.ForeignKey('Hotels', on_delete=models.CASCADE, related_name='rooms')
    status = models.CharField(choices=ROOM_STATUS, max_length=15)
    room_number = models.CharField(max_length=10, null=True)  # Removed `unique=True`

    # Discounts
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        help_text="Discount percentage (0-100%)"
    )

    # Ratings and reviews
    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text="Average rating (0-5)"
    )

    # Comments and replies
    comments = models.ManyToManyField('Comments', blank=True, related_name='rooms')

    # Room images (up to 12)
    image1 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image7 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image8 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image9 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image10 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image11 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image12 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image13 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image14 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image15 = models.ImageField(upload_to='room_images/', null=True, blank=True)

    # Additional fields
    description = models.TextField(null=True, blank=True, help_text="Detailed description of the room")
    heading = models.CharField(max_length=100, null=True, blank=True, help_text="Short heading for the room")
    food_facility = models.BooleanField(default=False, help_text="Indicates if food facility is available")
    parking = models.BooleanField(default=False, help_text="Indicates if parking is available")
    extra_person_charges = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        default=0.0, 
        validators=[MinValueValidator(0.0)], 
        help_text="Charges for extra person"
    )

    # Amenities
    comfortable_bed = models.BooleanField(default=False, help_text="Indicates if the room has a comfortable bed")
    private_bathroom = models.BooleanField(default=False, help_text="Indicates if the room has a private bathroom")
    wifi = models.BooleanField(default=False, help_text="Indicates if Wi-Fi is available")
    ac = models.BooleanField(default=False, help_text="Indicates if air conditioning is available")
    fan = models.BooleanField(default=False, help_text="Indicates if a fan is available")
    heater = models.BooleanField(default=False, help_text="Indicates if a heater is available")
    cleanliness = models.BooleanField(default=False, help_text="Indicates regular cleanliness")
    safety_security = models.BooleanField(default=False, help_text="Indicates if safety and security features are present")
    entertainment_options = models.BooleanField(default=False, help_text="Indicates if entertainment options are available")
    laundry_facility = models.BooleanField(default=False, help_text="Indicates if laundry facilities are available")
    outdoor_balcony = models.BooleanField(default=False, help_text="Indicates if an outdoor balcony is available")
    parking_area = models.BooleanField(default=False, help_text="Indicates if a parking area is available")
    food_facility = models.BooleanField(default=False, help_text="Indicates if a food facility is available")
    convenient_location = models.BooleanField(default=False, help_text="Indicates if the location is convenient")
    concierge_service = models.BooleanField(default=False, help_text="Indicates if concierge service is available")

    # Check-in and check-out times
    check_in_time = models.TimeField(null=True, blank=True, help_text="Check-in time (HH:MM AM/PM)")
    check_out_time = models.TimeField(null=True, blank=True, help_text="Check-out time (HH:MM AM/PM)")

    # Languages spoken by staff
    LANGUAGES_SPOKEN = (
        ("english", "English"),
        ("marathi", "Marathi"),
        ("hindi", "Hindi"),
    )
    languages_spoken = models.CharField(
        max_length=50, 
        choices=LANGUAGES_SPOKEN, 
        default="marathi",
        help_text="Languages spoken by staff"
    )

    def discounted_price(self):
        """Calculate price after applying the discount."""
        if self.discount > 0:
            return self.price - (self.price * (self.discount / Decimal(100)))
        return self.price

    def saved_money(self):
        """Calculate the saved amount due to the discount."""
        if self.discount > 0:
            return self.price * (self.discount / Decimal(100))
        return Decimal(0)

    def total_money(self):
        discounted_total = self.discounted_price()
        return discounted_total + (self.extra_person_charges or Decimal('0'))

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number} ({self.get_room_type_display()})"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['hotel', 'room_type', 'room_number'], name='unique_hotel_room_type_number')
        ]


class Comments(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='room_comments')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming default User model
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.room}"

class Replies(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming default User model
    reply_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.username} on {self.comment}"

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username


