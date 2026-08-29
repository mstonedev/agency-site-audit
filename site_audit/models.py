class AuditResult:
    def __init__(
        self,
        url: str,
        status_code: int,
        response_time_ms: float,
        is_https: bool,
        title: str | None,
        has_meta_description: bool,
        image_count: int,
        images_missing_alt: int,
        h1_count: int
        ):
        
        self.url = url
        self.status_code = status_code
        self.response_time_ms = response_time_ms
        self.is_https = is_https
        self.title = title
        self.has_meta_description = has_meta_description
        self.image_count = image_count
        self.images_missing_alt = images_missing_alt
        self.h1_count = h1_count
        
    def calculate_score(self) -> int:
        
        if self.url is None:
            return 0
        score = 100
        if self.status_code >= 400:
            return 0
        if 300 <= self.status_code < 400:
            score -= 10
        if not self.is_https:
            score -= 15
        if not self.title:
            score -= 15
        if not self.has_meta_description:
            score -= 10
        if self.h1_count == 0:
            score -= 10
        elif self.h1_count > 1:
            score -= 5
        if self.image_count > 0:
            score -= round(
                (self.images_missing_alt / self.image_count) * 20
            )
            
        return max(0, score)