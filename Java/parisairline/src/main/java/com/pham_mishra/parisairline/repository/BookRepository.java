package com.pham_mishra.parisairline.repository;

import com.pham_mishra.parisairline.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BookRepository extends JpaRepository<Book, Long> {
}

