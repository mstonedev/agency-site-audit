from site_audit.models import AuditResult

def test_healthy_audit_has_perfect_score() -> None:
    audit = AuditResult(
        url='https://google.com',
        status_code=200,
        response_time_ms=125.0,
        is_https=True,
        title="Example",
        has_meta_description=True,
        image_count=0,
        images_missing_alt=0,
        h1_count=1
    )
    
    score = audit.calculate_score()
    
    assert score == 100
    
def test_missing_quality_signals_reduce_score() -> None:
    audit = AuditResult(
        url='http://google.com',
        status_code=200,
        response_time_ms=1500.0,
        is_https=False,
        title=None,
        has_meta_description=False,
        image_count=0,
        images_missing_alt=0,
        h1_count=0
    )
        
    score = audit.calculate_score()
        
    assert score == 50