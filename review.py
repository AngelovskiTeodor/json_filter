from datetime import datetime

class ReviewDTO:
    def __init__(self,
                    id,
                    reviewId,
                    numLikes,
                    numComments,
                    numShares,
                    rating,
                    reviewCreatedOn,
                    reviewCreatedOnDate,
                    reviewCreatedOnTime,
                    reviewerId,
                    reviewerUrl,
                    reviewerName,
                    reviewerEmail,
                    sourceType,
                    isVerified,
                    source,
                    sourceName,
                    sourceId,
                    tags,
                    href,
                    logoHref,
                    photos,):
        self.id = id
        self.reviewId = reviewId
        self.numLikes = int(numLikes)
        self.numComments = int(numComments)
        self.numShares = int(numShares)
        self.rating = int(rating)
        self.reviewCreatedOn = reviewCreatedOn
        self.reviewCreatedOnDate = datetime.strptime(reviewCreatedOnDate, '%Y-%m-%dT%H:%M:%S+00:00') #example: "2021-01-25T13:00:35+00:00"
        self.reviewCreatedOnTime = reviewCreatedOnTime
        self.reviewerId = reviewerId
        self.reviewerUrl = reviewerUrl
        self.reviewerName = reviewerName
        self.reviewerEmail = reviewerEmail
        self.sourceType = sourceType
        self.isVerified = isVerified
        self.source = source
        self.sourceName = sourceName
        self.sourceId = sourceId
        self.tags = tags
        self.href = href
        self.logoHref = logoHref
        self.photos = photos


class DescriptiveReviewDTO(ReviewDTO):
    def __init__(self,
                    id,
                    reviewId,
                    reviewFullText,
                    reviewText,
                    numLikes,
                    numComments,
                    numShares,
                    rating,
                    reviewCreatedOn,
                    reviewCreatedOnDate,
                    reviewCreatedOnTime,
                    reviewerId,
                    reviewerUrl,
                    reviewerName,
                    reviewerEmail,
                    sourceType,
                    isVerified,
                    source,
                    sourceName,
                    sourceId,
                    tags,
                    href,
                    logoHref,
                    photos
                ):
        super().__init__(
                    id,
                    reviewId,
                    numLikes,
                    numComments,
                    numShares,
                    rating,
                    reviewCreatedOn,
                    reviewCreatedOnDate,
                    reviewCreatedOnTime,
                    reviewerId,
                    reviewerUrl,
                    reviewerName,
                    reviewerEmail,
                    sourceType,
                    isVerified,
                    source,
                    sourceName,
                    sourceId,
                    tags,
                    href,
                    logoHref,
                    photos,
        )
        self.reviewFullText = reviewFullText
        self.reviewText = reviewText

